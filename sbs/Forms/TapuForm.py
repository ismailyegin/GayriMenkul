from django import forms
from django.forms import ModelForm

from sbs.models.GTapu import GTapu


class TapuForm(ModelForm):
    class Meta:
        model = GTapu

        fields = (
            'year',
            'area',
            'parcel',
            'island',
            'neighborhood',
            'location',
            'town',
            'city',
            'country',

        )

        labels = {
            'year': 'Bina Yapım Yılı',
            'area': 'Kapalı Kullanım Alanı',
            'parcel': 'Parsel',
            'island': 'Ada',
            'neighborhood': 'Mahalle ',
            'location': 'Konum Bilgisi',
            'town': 'İlçe ',
            'city': 'Şehir',
            'country': 'Ülke',
        }
        widgets = {
            'year': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'area': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'parcel': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'island': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'kapalialan': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'location': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'adres': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'neighborhood': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'country': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', }),

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

        }
