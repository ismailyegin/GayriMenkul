from django import forms
from django.forms import ModelForm

from sbs.models.Gteskilat import Gteskilat


class GteskilatForm(ModelForm):
    class Meta:
        model = Gteskilat

        fields = (
            'depremderecesi',
            'yargiBolgesi',
            'merkeznufus',
            'yargiAlaniNufus',
            'acmyargiAlaniNufus',
            'city',
            'teskilatturu',
            'sirano',
            'town',
            'bamcity',
            'bamtown',
            'acmcity',
            'acmtown',
            'bimcity',
            'bimtown',

            'ilkDereceAdliYargiHakimSayisi',
            'ilkDereceAdliYargiSavcıSayisi',
            'ilkderecePersonelSayisi',
            'bolgeAdliyeHakimSayisi',
            'bolgeAdliyeSavcıSayisi',
            'bolgeAdliyePersonelSayisi',

            'bolgeIdaremahkemesiHakimSayisi',
            'bolgeIdareMahkemsiPersonelSayisi',
            'idareveVergiMahkemeleriHakimSayisi',
            'idariVergiMahkemeleriPersonelSayisi',



        )

        labels = {
            'depremderecesi': 'Deprem Derecesi',
            'yargiBolgesi': 'Yargı Bölgesi',

            'merkeznufus': 'MERKEZ NÜFUSU',
            'yargiAlaniNufus': 'ARGI ALANI NÜFUSU',
            'acmyargiAlaniNufus': 'ACM YARGI ALANI NÜFUSU',


            'city': 'Şehir',
            'teskilatturu': 'Teşkilat Türü',
            'sirano': 'Sıra Numarası',
            'town': 'ilçe',
            'bamcity': 'BAM Şehir',
            'bamtown': "BAM İlçe",
            'acmcity': "ACM Şehir",
            'acmtown': "ACM İlçe",
            'bimcity': "BİM Şehir",
            'bimtown': "BİM İlçe",

            'ilkDereceAdliYargiHakimSayisi': 'İLK DERECE ADLİ YARGI HÂKİM SAYISI',
            'ilkDereceAdliYargiSavcıSayisi': "İLK DERECE ADLİ YARGI SAVCI SAYISI",
            'ilkderecePersonelSayisi': "İLK DERECE PERSONEL SAYISI",
            'bolgeAdliyeHakimSayisi': '"BÖLGE ADLİYE MAHKEMESİ HÂKİM SAYISI"',
            'bolgeAdliyeSavcıSayisi': 'BÖLGE ADLİYE MAHKEMESİ SAVCI SAYISI',
            'bolgeAdliyePersonelSayisi': 'BÖLGE ADLİYE PERSONEL SAYISI',
            'bolgeIdaremahkemesiHakimSayisi': 'BÖLGE İDARE MAHKEMESİ HÂKİM SAYISI',
            'bolgeIdareMahkemsiPersonelSayisi': 'BÖLGE İDARE MAHKEMESİ PERSONEL SAYISI',
            'idareveVergiMahkemeleriHakimSayisi': 'İDARE VE VERGİ MAHKEMELERİ HÂKİM SAYISI',
            'idariVergiMahkemeleriPersonelSayisi': 'İDARE VE VERGİ MAHKEMELERİ PERSONEL SAYISI',


        }

        widgets = {

            'depremderecesi': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; ', }),
            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'town': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', }),
            'yargiBolgesi': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),
            'teskilatturu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; ', }),
            'yargiAlaniNufus': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

            'acmyargiAlaniNufus': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

            'merkeznufus': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'sirano': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'acmyargiAlaniNufus': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

            'bamcity': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', }),
            'bamtown': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', }),
            'bimcity': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', }),
            'bimtown': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', }),
            'acmcity': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', }),
            'acmtown': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', }),

            'ilkDereceAdliYargiHakimSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'ilkDereceAdliYargiSavcıSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'ilkderecePersonelSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'bolgeAdliyeHakimSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'bolgeAdliyeSavcıSayisi': forms.TextInput(attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'bolgeAdliyePersonelSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'bolgeIdaremahkemesiHakimSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'bolgeIdareMahkemsiPersonelSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'idareveVergiMahkemeleriHakimSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),
            'idariVergiMahkemeleriPersonelSayisi': forms.TextInput(
                attrs={'class': 'form-control', 'onkeypress': 'validate(event)'}),

        }
