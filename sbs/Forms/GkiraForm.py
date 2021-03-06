from django import forms
from django.forms import ModelForm

from sbs.models.Gkira import Gkira


class GkiraForm(ModelForm):
    class Meta:
        model = Gkira

        fields = (
            'sahibi',
            'onayTarihi',
            'tahsis_amaci',
            'sozlesmeTarihi',
            'sozlesmeSonTarihi',
            'kiralamaSuresi',
            'adres',
            'kapalialan',
            'kirabastarihi',

        )

        labels = {'sahibi': 'Sahibi',
                  'onayTarihi': ' Cumhurbaşkanlığı Onay Tarihi',
                  'tahsis_amaci': 'Kiralama Amacı',
                  'sozlesmeTarihi': 'Sözleşme Tarihi',
                  'sozlesmeSonTarihi': 'Sözleşme Bitiş Tarihi',
                  'kiralamaSuresi': 'Kiralama Süresi',
                  'kirabastarihi': 'Kira Başlangıç Tarihi',
                  'adres': 'Adres',
                  'kapalialan': 'Kapalı Alan ',

                  }

        widgets = {
            'sahibi': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'onayTarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),
            'sozlesmeTarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker7', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),
            'sozlesmeSonTarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker8', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),
            'kirabastarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker9', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),
            'adres': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'kapalialan': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'kiralamaSuresi': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'tahsis_amaci': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),

        }
