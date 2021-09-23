from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import generate_token
from django.core.mail import EmailMessage
import threading
from django.views.generic.base import View
from consignment.models import OrderConsignment
from .forms import ProfileForm


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Пожалуйста, активируйте ваш аккаунт'
    email_body = render_to_string('accounts/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email='pavel.k@dot-tech.ru',
                         to=[user.email]
                    )

    EmailThread(email).start()


# @auth_user_should_not_access
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        # login = request.POST.get('login')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 3:
            messages.add_message(request, messages.ERROR,
                                 'Пароль должен содержать не менее трех символов')

            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Пароли не совпадают')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Введите корректный email')
            context['has_error'] = True

        if not email:
            messages.add_message(request, messages.ERROR,
                                 'Введите email')
            context['has_error'] = True
            
        if Profile.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Этот email уже занят.')
            context['has_error'] = True
            return render(request, 'accounts/reglog.html', context, status=409)

        # if not login:
        #     messages.add_message(request, messages.ERROR,
        #                          'Введите логин')
        #     context['has_error'] = True
        
        # if Profile.objects.filter(login=login).exists():
        #     messages.add_message(request, messages.ERROR,
        #                          'Этот логин уже занят.')
        #     context['has_error'] = True
        #     return render(request, 'accounts/reglog.html', context, status=409)
        
        if context['has_error']:
            return render(request, 'accounts/reglog.html', context)
        
        user = Profile.objects.create_user(email=email, password=password)

        user.set_password(password)
        user.save()
        if not context['has_error']:
            send_activation_email(user, request)
            messages.add_message(request, messages.SUCCESS,
                                 'Вам на почту отправлено письмо со ссылкой для подтверждения')
            return redirect('login')
    return render(request, 'accounts/reglog.html')


# @auth_user_should_not_access
def login_user(request):
    if request.method == 'POST':
        context = {'data': request.POST}
        email = request.POST.get('email')
        password = request.POST.get('password')        
        user = authenticate(request, email=email, password=password)
        if user and user.is_active == False:
            messages.add_message(request, messages.ERROR,
                                 'Email не верифицирован. Пожалуйста, проверьте свой почтовый ящик.')
            print('no verified')
            return render(request, 'accounts/reglog.html', context, status=401)
        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Неверные данные')
            print('no')
            return render(request, 'accounts/reglog.html', context, status=401)
        login(request, user)
        messages.add_message(request, messages.SUCCESS,
                             f'Добро пожаловать, {user.__str__()}')
        print(f'Добро пожаловать, {user.__str__()}')
        return redirect('/')
    return render(request, 'accounts/reglog.html')


def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         'Вы вышли из аккаунта'
                    )
    return redirect(reverse('login'))


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Profile.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             'Email верифицирован, вы можете войти на сайт.')
        return redirect(reverse('login'))
    return render(request, 'accounts/reglog.html', {"user": user})


class PersonalCabinet(View):
    def get(self, request, id):
        user = Profile.objects.filter(id=id).first()
        orders = OrderConsignment.objects.select_related('user').filter(user=user)
        count_orders = orders.count()
        form = ProfileForm(instance=user)
        context = {
            'user': user,
            'form': form,
            'orders': orders,
            'count_orders': count_orders
        }
        return render(request, 'personal_cabinet.html', context)
    
    def post(self, request, id):
        updated_user = Profile.objects.filter(id=id).first()
        form = ProfileForm(request.POST, instance=updated_user)
        print(form.errors)
        if form.is_valid():
            updated_user.name = form.cleaned_data['name']
            updated_user.surname = form.cleaned_data['surname']
            updated_user.city = form.cleaned_data['city']
            updated_user.save()
            # updated_user.name = form.cleaned_data.get('name', None)
            # updated_user.surname = form.cleaned_data('surname', None)
            # updated_user.city = form.cleaned_data('city', None)
        return self.get(request, id)
    
def test(request):
    return render(request, 'test.html')