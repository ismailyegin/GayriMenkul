from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazlojmanForm(ModelForm):
    class Meta:
        model = Gtasinmaz

        fields = (
            'name',
            'sirano',
            'tkgmno',
            'definition',
            'tasinmazinTuru',
            'tahsisDurumu',
            'mustakil',
            'blockSayisi',
            'daireSayisi',
            'lojmanYapimYili',
            'lojmanturu',
            'daireAlaniNet',
            'daireBrut',
            'lojmanKullanim',
            'hDaireSayisi',
            'atvgdaireSayisi',
            'isDaireSayisi',
            'mDaireSayisi',
            'mSavciSayisi',
            'mAyriBlock',
            'blockDaire'

        )

        labels = {'name': 'Tanımı',
                  'sirano': 'Sıra numarası',
                  'tkgmno': 'Tkgm numarası',

                  'tasinmazinTuru': 'Taşınmazın Türü',
                  'definition': 'Açıklama',
                  'tahsisDurumu': 'Tahsis Durumu',
                  'mustakil': 'Lojman Mülkiyet Durumu',
                  'blockSayisi': ' Blok Sayısı',
                  'daireSayisi': 'Daire Sayısı ',
                  'lojmanYapimYili': 'Lojman Yapım Yılı',
                  'lojmanturu': 'Lojman Turu ',
                  'daireBrut': ' Daire Kapalı Kullanim Alanı Brut',
                  'daireAlaniNet': 'Daire Kapalı Kullanim Alanı Net',
                  'lojmanKullanim': 'Lojman Kullanim Durumu',
                  'hDaireSayisi': 'Hazine Lojman Daire Sayısı',
                  'atvgdaireSayisi': 'Atgv Lojmanı Daire Sayısı',
                  'isDaireSayisi': 'İs yurtlari Daire Sayısı ',
                  'mDaireSayisi': 'Mahaldeki Toplam Daire Sayisi',
                  'mSavciSayisi': 'Mahaldeki Toplam Hakim ve Savcı Sayisi',
                  'mAyriBlock': 'Müstakil Ayrı Blok',
                  'blockDaire': 'Blok İçinde Daire',


                  }

        widgets = {

            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', 'required': 'required'}),
            'tahsisDurumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', 'required': 'required'}),
            'mustakil': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; ', }),
            'sirano': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'tkgmno': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control ', }),
            'definition': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2'}),

            'blockSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'daireSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'lojmanYapimYili': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker3', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'lojmanturu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                              'style': 'width: 100%; ', }),
            'daireBrut': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'daireAlaniNet': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'lojmanKullanim': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                        'style': 'width: 100%; ', }),
            'hDaireSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'atvgdaireSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'isDaireSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'mDaireSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'mSavciSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

            'mAyriBlock': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                     'style': 'width: 100%; ', }),
            'blockDaire': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),


        }
