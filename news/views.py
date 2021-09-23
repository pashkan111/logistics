from django.views import generic, View
from .forms import NewsForm
from news.models import Post
from django.shortcuts import redirect, render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'news_detail.html'
    
class FormView(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'test.html', {'form': form})
    
    def post(self, request):
        form = NewsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/') 