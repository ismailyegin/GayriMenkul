from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GtasinmazSearchForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False

        self.fields['tkgmno'].required = False
        self.fields['sirano'].required = False
        self.fields['tasinmazinTuru'].required = False

    class Meta:
        model = Gtasinmaz

        fields = (
            'name', 'sirano', 'tkgmno', 'tasinmazinTuru', 'tahsisDurumu')

        labels = {'name': 'Tanımı',
                  'sirano': 'Sıra numarası',

                  'tkgmno': 'Tkgm numarası',
                  'tasinmazinTuru': 'Tasinmazin Türü',
                  'tahsisDurumu': 'Tahsis Durumu'

                  }

        widgets = {
            'yapiMalitet': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'sirano': forms.TextInput(
                attrs={'class': 'form-control '}),
            'tkgmno': forms.TextInput(
                attrs={'class': 'form-control '}),

            'name': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', }),
            'tahsisDurumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),

        }
