from django import forms
from .models import contact, ResumeModel


class DocumentForm(forms.ModelForm):
    class Meta:
        model= ResumeModel
        fields = ['pdf']