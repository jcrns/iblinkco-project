from django import forms
from homepage.models import Contactus

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
