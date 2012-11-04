from django import forms
from django.forms import ModelForm, Textarea, Select

from django.contrib.localflavor.es.forms import * 
from django.contrib.localflavor.es.forms import ESProvinceSelect

from .models import Gbeers

class GbeersForm(forms.ModelForm):
#    provincia = forms.SelectField(widget=EsProvinceSelect())

    class Meta:
        model = Gbeers
        widgets = {
#            'provincia': Textarea(attrs={'cols': 80, 'rows': 20}),    
#            'provincia': Select(ESProvinceSelect())    
        }
