from django import forms
from django.forms import ModelForm

from sbs.models.Gteskilat import Gteskilat


class GteskilatSearchForm(ModelForm):
    class Meta:
        model = Gteskilat

        fields = (
            'yargiBolgesi',
            'city',
            'town',
            'teskilatturu',
            'acm',
            'bam',
            'bim',

        )

        labels = {
            'depremderecesi': 'Deprem Derecesi',
            'yargiBolgesi': 'Yargı Bölgesi',
            'merkeznufus': 'Merkez Nufusu',
            'city': 'İl',
            'town': 'İlçe',
            'teskilatturu': 'Teşkilat Türü',
            'acm': 'ACM',
            'bam': 'BAM',
            'bim': 'BİM',

        }

        widgets = {


            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'yargiBolgesi': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),

            'acm': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                       'style': 'width: 100%; ', }),
            'bam': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                       'style': 'width: 100%; ', }),
            'bim': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                       'style': 'width: 100%; ', }),
            'teskilatturu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),

        }

    def __init__(self, *args, **kwargs):
        super(GteskilatSearchForm, self).__init__(*args, **kwargs)
        self.fields['city'].required = False
        self.fields['yargiBolgesi'].required = False
        self.fields['town'].required = False
        self.fields['teskilatturu'].required = False
        self.fields['acm'].required = False
        self.fields['bam'].required = False
        self.fields['bim'].required = False
