from django import forms
from django.forms import ModelForm

from sbs.models.Gbolge import Gbolge


class GBimForm(ModelForm):
    class Meta:
        model = Gbolge

        fields = (

            'town',
            'city',

        )

        labels = {
            'town': 'Bim -İlçe ',
            'city': 'Bim -Şehir',
        }
        widgets = {

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

        }
