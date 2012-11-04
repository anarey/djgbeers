from django import forms
from django.forms import ModelForm

from django.contrib.localflavor.es.forms import * 


from .models import Gbeers

class GbeersForm(forms.ModelForm):

    class Meta:
        model = Gbeers

