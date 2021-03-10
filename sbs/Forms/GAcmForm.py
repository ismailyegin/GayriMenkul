from django import forms
from django.forms import ModelForm

from sbs.models.Gbolge import Gbolge


class GAcmForm(ModelForm):
    class Meta:
        model = Gbolge

        fields = (

            'town',
            'city',

        )

        labels = {
            'town': 'Acm İlçe ',
            'city': 'Acm Şehir',

        }
        widgets = {

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', 'name': "acmcity"}),

            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', 'name': 'acmtown'}),

        }
