from django import forms
from django.forms import ModelForm

from sbs.models.Gteskilat import Gteskilat


class GteskilatSearchForm(ModelForm):
    class Meta:
        model = Gteskilat

        fields = (
            'depremderecesi',
            'yargiBolgesi',
            'city',
            'town'

        )

        labels = {
            'depremderecesi': 'Deprem Derecesi',
            'yargiBolgesi': 'Yargı Bölgesi',
            'merkeznufus': 'Merkez Nufusu',
            'city': 'İl',
            'town': 'İlçe'

        }

        widgets = {

            'depremderecesi': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', }),
            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'yargiBolgesi': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),

            'merkeznufus': forms.TextInput(
                attrs={'class': 'form-control ', }),


        }

    def __init__(self, *args, **kwargs):
        super(GteskilatSearchForm, self).__init__(*args, **kwargs)
        self.fields['depremderecesi'].required = False
        self.fields['city'].required = False
        self.fields['yargiBolgesi'].required = False
        self.fields['town'].required = False
