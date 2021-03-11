from django import forms
from django.forms import ModelForm

from sbs.models.Gtasinmaz import Gtasinmaz


class GtasinmazlojmanForm(ModelForm):
    class Meta:
        model = Gtasinmaz

        fields = (
            'name', 'sirano', 'tkgmno',
            'arsaDegeri', 'definition',
            'tasinmazinTuru',
            'tahsisDurumu',
            'mustakil',
            'blockSayisi',
            'daireSayisi',
            'lojmanYapimYili',
            'lojmanturu',
            'daireKapaliKulllanimAlaniBrut',
            'daireKapaliKulllanimAlaniNet',
            'lojmanKullanimDurumu',
            'hazinelojmaniDaireSayisi',
            'atvglojmaniDaireSayisi',
            'isyurtlariDaireSayisi',
            'mahaldekiToplamDaireSayisi',
            'mahaldekiToplamHakimSavcıSayisi',
            'arsayuzolcumu',
            'mustakilAyriBlock',
            'blockicindeDaire'

        )

        labels = {'name': 'Tanımı',
                  'sirano': 'Sıra numarası',
                  'tkgmno': 'Tkgm numarası',

                  'tasinmazinTuru': 'Taşınmazın Türü',
                  'definition': 'Açıklama',
                  'tahsisDurumu': 'Tahsis Durumu',
                  'mustakil': 'Lojman Mülkiyet Durumu',
                  'blockSayisi': ' Block Sayısı',
                  'daireSayisi': 'Daire Sayısı ',
                  'lojmanYapimYili': 'Lojman Yapım Yılı',
                  'lojmanturu': 'Lojman Turu ',
                  'daireKapaliKulllanimAlaniBrut': ' Daire Kapalı Kullanim Alanı Brut',
                  'daireKapaliKulllanimAlaniNet': 'Daire Kapalı Kullanim Alanı Net',
                  'lojmanKullanimDurumu': 'Lojman Kullanim Durumu',
                  'hazinelojmaniDaireSayisi': 'Hazine Lojman Daire Sayısı',
                  'atvglojmaniDaireSayisi': 'Atvg Lojmanı Daire Sayısı',
                  'isyurtlariDaireSayisi': 'İs yurtlari Daire Sayısı ',
                  'mahaldekiToplamDaireSayisi': 'Mahaldeki Toplam Daire Sayisi',
                  'mahaldekiToplamHakimSavcıSayisi': 'Mahaldeki Toplam Hakim ve Savcı Sayisi',
                  'arsayuzolcumu': 'Arsa Yüzölçümü',
                  'mustakilAyriBlock': 'Müstakil Ayrı Blok',
                  'blockicindeDaire': 'Blok İçinde Daire',


                  }

        widgets = {

            'tasinmazinTuru': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', 'required': 'required'}),
            'tahsisDurumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),
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
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'lojmanturu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                              'style': 'width: 100%; ', }),
            'daireKapaliKulllanimAlaniBrut': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'daireKapaliKulllanimAlaniNet': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'lojmanKullanimDurumu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                        'style': 'width: 100%; ', }),
            'hazinelojmaniDaireSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'atvglojmaniDaireSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'isyurtlariDaireSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'mahaldekiToplamDaireSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'mahaldekiToplamHakimSavcıSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'arsayuzolcumu': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

            'mustakilAyriBlock': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                     'style': 'width: 100%; ', }),
            'blockicindeDaire': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),


        }
