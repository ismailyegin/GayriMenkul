from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazArsaForm(ModelForm):
    class Meta:
        model = Gtasinmaz

        fields = (
            'name', 'sirano', 'tkgmno',
            'arsaDegeri', 'definition',
            'tasinmazinTuru',
            'tahsisDurumu',
            'tahsisAmaci',
        )

        labels = {'name': 'Tanımı',
                  'sirano': 'Sıra numarası',
                  'tkgmno': 'Tkgm numarası',

                  'tasinmazinTuru': 'Taşınmazın Türü',
                  'definition': 'Açıklama',
                  'tahsisDurumu': 'Tahsis Durumu ',
                  'tahsisAmaci': 'Tahsis Amacı'
                  }

        widgets = {

            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', 'required': 'required'}),
            'tahsisAmaci': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%; '}),
            'tahsisDurumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', 'required': 'required'}),
            'sirano': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'tkgmno': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'definition': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2'}),

        }
