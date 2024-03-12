from django import forms
from technology.models import tech_model


class techmodelform(forms.ModelForm):
    class Meta:
        model=tech_model
        fields = ['topic', 'text']