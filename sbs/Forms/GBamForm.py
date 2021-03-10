from django import forms
from django.forms import ModelForm

from sbs.models.Gbolge import Gbolge


class GBamForm(ModelForm):
    class Meta:
        model = Gbolge

        fields = (

            'town',
            'city',

        )

        labels = {
            'town': 'Bam -İlçe ',
            'city': 'Bam -Şehir',

        }
        widgets = {

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

        }
