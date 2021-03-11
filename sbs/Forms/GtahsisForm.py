from django import forms
from django.forms import ModelForm

from sbs.models.Gtahsis import Gtahsis


class GtahsisForm(ModelForm):
    class Meta:
        model = Gtahsis

        fields = ('tahsisTarihi',
                  'tahsisSuresi',
                  'tahsis_amaci',
                  'tahsis_kurum',
                  'emsal')

        labels = {'tahsisTarihi ': 'Tahsis Tarihi',
                  'tahsisSuresi ': 'Tahsis Süresi',
                  'tahsis_amaci ': 'Tahsis Amacı',
                  'tahsis_kurum ': 'Tahsis Eden Kurum',
                  'emsal ': 'Emsal',

                  }

        widgets = {
            'emsal': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'tahsisSuresi': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'tahsis_amaci': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),
            'tahsis_kurum': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'tahsisTarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),

        }
