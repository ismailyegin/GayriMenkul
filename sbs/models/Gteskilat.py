from django.db import models

from sbs.models.City import City
from sbs.models.Gbolge import Gbolge
from sbs.models.Town import Town


class Gteskilat(models.Model):
    D1 = "1.DERECE"
    D2 = "2.DERECE"
    D3 = "3.DERECE"
    D4 = "4.DERECE"
    D5 = "5.DERECE"

    DEPREM_DERECE = (

        (D1, '1.DERECE'),
        (D2, '2.DERECE'),
        (D3, '3.DERECE'),
        (D4, '4.DERECE'),
        (D5, '5.DERECE'),

    )

    B1 = "1.BÖLGE"
    B2 = "2.BÖLGE"
    B3 = "3.BÖLGE"
    B4 = "4.BÖLGE"
    B5 = "5.BÖLGE"

    Yargi_bolgesi = (

        (B1, '1.BÖLGE'),
        (B2, '2.BÖLGE'),
        (B3, '3.BÖLGE'),
        (B4, '4.BÖLGE'),
        (B5, '5.BÖLGE'),
    )

    C1 = "AĞIR CEZA CUMHURİYET BAŞSAVCILIĞI"
    C2 = "ASLİYE CEZA CUMHURİYET BAŞSAVCILIĞI"
    C3 = "DİĞER MÜLHAKAT"
    teskilatturu = (

        (C1, 'AĞIR CEZA CUMHURİYET BAŞSAVCILIĞI'),
        (C2, 'ASLİYE CEZA CUMHURİYET BAŞSAVCILIĞI'),
        (C3, 'DİĞER MÜLHAKAT'),

    )

    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)

    depremderecesi = models.CharField(max_length=128, verbose_name='deprem derecesi', choices=DEPREM_DERECE, null=True,
                                      blank=True)
    yargiBolgesi = models.CharField(max_length=128, verbose_name='Yargi Bölgesi', choices=Yargi_bolgesi, null=True,
                                    blank=True)
    merkeznufus = models.IntegerField(blank=True, null=True, )
    yargiAlaniNufus = models.IntegerField(blank=True, null=True, )
    acmyargiAlaniNufus = models.IntegerField(blank=True, null=True, )



    kobilid = models.IntegerField(null=True, blank=True, default=2)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name='sehir', null=False, blank=False)
    town = models.ForeignKey(Town, on_delete=models.SET_NULL, verbose_name='ilce', null=True, blank=True)
    sirano = models.IntegerField(blank=True, null=True)

    teskilatturu = models.CharField(max_length=128, verbose_name='teskilatturu', choices=teskilatturu, null=True,
                                    blank=True)

    bam = models.ForeignKey(Gbolge, on_delete=models.SET_NULL, verbose_name='bam', null=True, blank=True)
    bim = models.ForeignKey(Gbolge, on_delete=models.SET_NULL, verbose_name='bim', null=True, blank=True)
    acm = models.ForeignKey(Gbolge, on_delete=models.SET_NULL, verbose_name='acm', null=True, blank=True)
    # adli yargı
    ilkDereceAdliYargiHakimSayisi = models.IntegerField(blank=True, null=True, )
    ilkDereceAdliYargiSavcıSayisi = models.IntegerField(blank=True, null=True, )
    ilkderecePersonelSayisi = models.IntegerField(blank=True, null=True, )
    bolgeAdliyeHakimSayisi = models.IntegerField(blank=True, null=True, )
    bolgeAdliyeSavcıSayisi = models.IntegerField(blank=True, null=True, )
    bolgeAdliyePersonelSayisi = models.IntegerField(blank=True, null=True, )

    # idari yargı
    bolgeIdaremahkemesiHakimSayisi = models.IntegerField(blank=True, null=True, )
    bolgeIdareMahkemsiPersonelSayisi = models.IntegerField(blank=True, null=True, )
    idareveVergiMahkemeleriHakimSayisi = models.IntegerField(blank=True, null=True, )
    idariVergiMahkemeleriPersonelSayisi = models.IntegerField(blank=True, null=True, )

    # bam=models.ForeignKey(Gbolge,on_delete=models.SET_NULL,verbose_name='bam',null=True,blank=True)
    # bim=models.ForeignKey(Gbolge,on_delete=models.SET_NULL,verbose_name='bim',null=True,blank=True)
    # acm=models.ForeignKey(Gbolge,on_delete=models.SET_NULL,verbose_name='acm',null=True,blank=True)

    #
    # UsageArea = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0)
