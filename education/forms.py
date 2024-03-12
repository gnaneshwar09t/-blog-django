from django import forms
from education.models import edu_model


class edumodelform(forms.ModelForm):
    class Meta:
        model=edu_model
        fields = ['topic', 'text']

        