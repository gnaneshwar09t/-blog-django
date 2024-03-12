from django import forms
from entertainment.models import ent_model


class entmodelform(forms.ModelForm):
    class Meta:
        model=ent_model
        fields = ['topic', 'text']