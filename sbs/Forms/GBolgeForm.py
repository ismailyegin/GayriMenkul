from django import forms
from django.forms import ModelForm

from sbs.models.Gbolge import Gbolge


class GbolgeForm(ModelForm):
    class Meta:
        model = Gbolge

        fields = (

            'town',
            'city',
            'name',
            'type'

        )

        labels = {
            'town': 'İlçe ',
            'city': 'İl',
            'name': 'Tanımı',
            'type': 'Tipi'
        }
        widgets = {

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'type': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'name': forms.TextInput(
                attrs={'class': 'form-control ', }),


        }
