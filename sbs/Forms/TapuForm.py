from django import forms
from django.forms import ModelForm

from sbs.models.GTapu import GTapu


class TapuForm(ModelForm):
    class Meta:
        model = GTapu

        fields = (

            'parcel',
            'island',
            'neighborhood',
            'town',
            'city',
            'arsayuzolcumu'
        )

        labels = {

            'parcel': 'Parsel',
            'island': 'Ada',
            'neighborhood': 'Mahalle ',
            'town': 'İlçe ',
            'city': 'Şehir',
            'arsayuzolcumu': 'Arsa Yüz Ölçümü',

        }
        widgets = {
            'parcel': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'island': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'kapalialan': forms.TextInput(
                attrs={'class': 'form-control ', }),


            'adres': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'neighborhood': forms.TextInput(
                attrs={'class': 'form-control ', }),


            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),

            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'arsayuzolcumu': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

        }
