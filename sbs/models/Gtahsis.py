from django.db import models

from sbs.models.Gkurum import Gkurum


class Gtahsis(models.Model):
    CIK = 'Ceza İnfaz Kurumu'
    AB = 'Adalet Binası'
    AT = 'Adli Tıp'
    BAM = 'Bölge Adliye Mahkemesi'
    BIM = 'Bölge İdare Mahkemesi'
    DS = 'Denetimli Serbestlik'
    PEM = 'Personel Eğitim Merkezi'
    BB = 'Bakanlık Binası'
    LOJMAN = 'Lojman'
    SOS = "SOSYAL TESİS "
    HAK = "HAKİM EVİ"

    DIGER = 'Diğer'

    TAHSİS_AMACİ = (
        (CIK, 'Ceza İnfaz Kurumu'),
        (AB, 'Adalet Binası'),
        (AT, 'Adli Tıp'),
        (BAM, 'Bölge Adliye Mahkemesi'),
        (BIM, 'Bölge İdare Mahkemesi'),
        (DS, 'Denetimli Serbestlik'),
        (BB, 'Bakanlık Bİnası'),
        (PEM, 'Personel Eğitim Merkezi'),
        (LOJMAN, 'Lojman'),

        (SOS, 'Sosyal Tesis'),
        (HAK, 'Hakim Evi'),
        (DIGER, 'Diğer'),
    )
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)

    tahsisTarihi = models.DateTimeField(null=True, blank=True)
    tahsisSuresi = models.CharField(max_length=128, verbose_name='Tahsis Süresi', null=True, blank=True)
    tahsis_amaci = models.CharField(max_length=128, verbose_name='Proje Cinsi', choices=TAHSİS_AMACİ, default=AB)
    tahsis_kurum = models.ForeignKey(Gkurum, on_delete=models.SET_NULL, verbose_name='Tahsis Eden Kurum', null=True,
                                     blank=True)
    emsal = models.CharField(max_length=128, verbose_name='Emsal', null=True, blank=True)
