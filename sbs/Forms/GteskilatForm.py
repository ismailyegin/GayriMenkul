from django import forms
from django.forms import ModelForm

from sbs.models.Gteskilat import Gteskilat


class GteskilatForm(ModelForm):
    class Meta:
        model = Gteskilat

        fields = (
            'depremderecesi',
            'yargiBolgesi',
            'merkeznufus',
            'yargiAlaniNufus',
            'agirCezaMerkezi',
            'asliyeCezaMerkezi',
            'hakim_sayisi',
            'savci_sayisi',
            'personel_sayisi',
            'mulhakat',
            'city'

        )

        labels = {
            'depremderecesi': 'Deprem Derecesi',
            'yargiBolgesi': 'Yargı Bölgesi',
            'merkeznufus': 'Merkez Nufusu',
            'yargiAlaniNufus': 'Yargı Alanı',
            'agirCezaMerkezi': 'Agır Ceza Merkezi',
            'asliyeCezaMerkezi': 'Asliye Ceza Merkezi',
            'hakim_sayisi': 'Hakim Sayısı',
            'savci_sayisi': 'Savcı Sayısı ',
            'personel_sayisi': 'Personel Sayısı',
            'mulhakat': 'Mülhakat',
            'city': 'Şehir'

        }

        widgets = {

            'depremderecesi': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', }),
            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'yargiBolgesi': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),

            'merkeznufus': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'agirCezaMerkezi': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'yargiAlaniNufus': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'asliyeCezaMerkezi': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'hakim_sayisi': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'savci_sayisi': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'personel_sayisi': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'mulhakat': forms.TextInput(
                attrs={'class': 'form-control ', }),

        }
