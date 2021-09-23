from django.forms import ModelForm
from .models import Post


class NewsForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Post