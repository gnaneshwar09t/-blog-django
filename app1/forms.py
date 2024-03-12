from django import forms
from app1.models import model2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class samplemodelform(forms.ModelForm):
    class Meta:
        model=model2
        fields = ['category','topic', 'text']


class usermodelform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

