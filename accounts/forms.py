from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['phone'].widget.attrs['readonly'] = True
        self.fields['phone'].widget.attrs['max_length'] = 18
        
    class Meta:
        model = Profile
        fields = ("name", 'surname', 'email', 'phone', 'city')