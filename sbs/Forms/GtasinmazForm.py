from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazForm(ModelForm):
    class Meta:
        model = Gtasinmaz

        fields = (
            'name', 'sirano', 'block', 'floor', 'mulkiyet', 'tkgmno', 'UsageArea', 'tahsis_durumu',
            'arsaDegeri', 'yapiRaic', 'yapiMalitet',
            'tasinmazinTuru', 'definition', 'arsaTuru')

        labels = {'name': 'Tanımı',
                  'sirano': 'Sıra numarası',
                  'block': 'Blok Adeti',
                  'floor': 'Kat Sayısı',
                  'mulkiyet': 'Mülkiyet',
                  'tkgmno': 'Tkgm numarası',
                  'UsageArea': 'Kullanılan Alan (m2) ',
                  'tahsis_durumu': "Tahsis durumu",
                  'tasinmazinTuru': 'Taşınmazın Türü',
                  'definition': 'Açıklama',
                  'arsaDegeri': 'Arsa Degeri:',
                  'yapiMalitet': 'Yapı Maliyet degeri ',
                  'yapiRaic': 'Yapı Raiç Degeri',
                  'arsaTuru': 'Bina mı?'


                  }

        widgets = {
            'yapiMalitet': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'yapiRaic': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'arsaDegeri': forms.TextInput(
                attrs={'class': 'form-control ', }),

            'arsaTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; '}),

            'mulkiyet': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; ', 'required': 'required'}),
            'tahsis_durumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                 'style': 'width: 100%; ', 'required': 'required'}),
            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', 'required': 'required'}),
            'sirano': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'tkgmno': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'floor': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'block': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'UsageArea': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'name': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'definition': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2'}),

        }
