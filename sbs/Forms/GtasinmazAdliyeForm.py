from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazAdliyeForm(ModelForm):
    class Meta:
        model = Gtasinmaz

        fields = (
            'name',
            'sirano',
            'tkgmno',
            'definition',
            'tasinmazinTuru',

            'yapimyili',
            'edinimyili',
            'kapalikullanimalani',
            'blokadeti',
            'katadedi',
            'mustakil',
            'diger',
        )

        labels = {

            'name': 'Tanımı',
            'sirano': 'Sıra numarası',
            'tkgmno': 'Tkgm numarası',
            'tasinmazinTuru': 'Taşınmazın Türü',
            'definition': 'Açıklama',
            'yapimyili': 'YAPIM YILI ',
            'edinimyili': 'EDİNİM YILI',
            'kapalikullanimalani': "BRÜT KAPALI KULLANIM ALANI (m²)",
            'blokadeti': 'BLOK ADEDİ',
            'katadedi': "KAT ADEDİ",
            'mulkiyet': 'Mülkiyet',
            'mustakil': 'Müstakil',
            'diger': 'Diger',
        }

        widgets = {

            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', 'required': 'required'}),
            'mustakil': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; '}),
            'diger': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                         'style': 'width: 100%; '}),
            'sirano': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'tkgmno': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'definition': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2'}),

            'yapimyili': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'edinimyili': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker3', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'kapalikullanimalani': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'blokadeti': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'katadedi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

        }
