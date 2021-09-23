from django.shortcuts import render


from calculator.models import Calculate, Term, City

from consignment.models import OrderConsignment, OrderStatusConsignment
from tracking.models import Tracking

# Create your views here.

def landing_page(req):
    context = {
        # 'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'home.html', context)


def tracking_page(req):
    context = {
        # 'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'tracking.html', context)

def price_page(req):
    context = {
        # 'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'price.html', context)


def reglog(req):
    context = {
        # 'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, 'accounts/reglog.html', context)


def page_404(req):
    context = {
        # 'is_worker': req.user.groups.filter(name='worker').exists(),
    }
    return render(req, '404_page.html', context)


def db(request):
    queryset_track = Tracking.objects.all()
    queryset_order = OrderConsignment.objects.all()
    queryset_orderStatus = OrderStatusConsignment.objects.all()
    queryset_cities = City.objects.all()
    queryset_calc = Calculate.objects.all()
    queryset_term = Term.objects.all()
    context = {
        'calcs': queryset_calc,
        'terms': queryset_term,
        'tracks': queryset_track,
        'orders': queryset_order,
        'orderstatuss': queryset_orderStatus,
        'cities': queryset_cities,
    }
    return render(request, 'db.html', context)

def about(request):
    return render(request, 'about.html')