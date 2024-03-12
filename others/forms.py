from django import forms
from others.models import ot_model


class otmodelform(forms.ModelForm):
    class Meta:
        model=ot_model
        fields = ['topic', 'text']