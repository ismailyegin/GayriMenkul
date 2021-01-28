from django.db import models


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
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)

    depremderecesi = models.CharField(max_length=128, verbose_name='deprem derecesi', choices=DEPREM_DERECE, null=True,
                                      blank=True)
    yargiBolgesi = models.CharField(max_length=128, verbose_name='Yargi Bölgesi', choices=Yargi_bolgesi, null=True,
                                    blank=True)
    merkeznufus = models.IntegerField(blank=True, null=True, )
    yargiAlaniNufus = models.IntegerField(blank=True, null=True, )
    agirCezaMerkezi = models.CharField(max_length=128, blank=True, null=True, )
    asliyeCezaMerkezi = models.CharField(max_length=128, blank=True, null=True, )
    hakim_sayisi = models.CharField(max_length=128, blank=True, null=True, )
    savci_sayisi = models.IntegerField(blank=True, null=True, )
    personel_sayisi = models.IntegerField(blank=True, null=True, )
    mulhakat = models.CharField(max_length=128, blank=True, null=True, )
    #
    # UsageArea = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0)
