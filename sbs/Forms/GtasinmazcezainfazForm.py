from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazcezainfazForm(ModelForm):
    class Meta:
        model = Gtasinmaz

        fields = (
            'name',
            'sirano',
            'tkgmno',
            'arsaDegeri',
            'definition',
            'tasinmazinTuru',
            'yapimyili',
            'tipi',
            'kapasitesi',
            'brutKapaliAlan',
            'tahsisDurumu'

        )

        labels = {'name': 'Tanımı',
                  'sirano': 'Sıra numarası',
                  'tkgmno': 'Tkgm numarası',
                  'tasinmazinTuru': 'Taşınmazın Türü',
                  'definition': 'Açıklama',
                  'tipi': 'Tipi',
                  'kapasitesi': 'Kapasitesi',
                  'brutKapaliAlan': 'Brüt Kapali Kullanim Alanı',
                  'tahsisDurumu': 'Tahsis Durumu',
                  'yapimyili': 'Yapım Yılı ',
                  }

        widgets = {

            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', 'required': 'required'}),
            'sirano': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'tkgmno': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'definition': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2'}),

            'tipi': forms.TextInput(attrs={'class': 'form-control', }),
            'kapasitesi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'brutKapaliAlan': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'tahsisDurumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', 'required': 'required'}),
            'yapimyili': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker3', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),

        }
