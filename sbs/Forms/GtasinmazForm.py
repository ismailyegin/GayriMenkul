from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazForm(ModelForm):
    class Meta:
        model = Gtasinmaz

        fields = (
            'name', 'sirano', 'tkgmno',
            'arsaDegeri', 'definition',
            'tasinmazinTuru',
            'tahsisDurumu')

        labels = {'name': 'Tanımı',
                  'sirano': 'Sıra numarası',
                  'tkgmno': 'Tkgm numarası',

                  'tasinmazinTuru': 'Taşınmazın Türü',
                  'definition': 'Açıklama',
                  'tahsisDurumu': 'Tahsis Durmumu',
                  }

        widgets = {


            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', 'required': 'required'}),
            'sirano': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'tkgmno': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'definition': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2'}),

            'tahsisDurumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', 'required': 'required'}),

        }
