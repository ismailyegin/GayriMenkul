from django.db import models

from sbs.models.EPOffer import EPOffer
from sbs.models.GTapu import GTapu
from sbs.models.Gkira import Gkira
from sbs.models.Gkurum import Gkurum
from sbs.models.Gtahsis import Gtahsis
from sbs.models.GtasinmazBinaAltTur import GtasinmazAltTur
from sbs.models.GtasinmazBinaUstTur import GtasinmazUstTur
from sbs.models.GtasinmazDocument import GtasinmazDocument


class Gtasinmaz(models.Model):
    # TahsisliArsa = "Tahsisli Arsa"
    # Kira = "Kiralık"
    #
    # TahsisDurumu = (
    #
    #     (TahsisliArsa, 'Tahsisli Arsa '),
    #     (Kira, 'Kiralık'),
    # )

    Bina = "Bina"
    Arsa = "Arsa"

    ArsaDurumu = (

        (Bina, 'Bina'),
        (Arsa, 'Arsa'),
    )

    Hazine = 'HAZİNE'
    Hukumet_konagi_icinde = "HÜKÜMET KONAGI İÇERİSİNDE"
    Hukumet_konagi_ayri = "HÜKÜMET KONAGI AYRİ BLOK"
    Is_yurtlari = "İŞ YURTLARI"
    Diger = "DİĞER KAMU KURUM KURULUŞLARINDAN TAHSİSLİ "
    Atvg = 'ATVG'
    Kiralik = "KİRALIK"

    Mustakil = (
        (Hazine, 'HAZİNE'),
        (Is_yurtlari, 'İŞ YURTLARI'),
        (Atvg, 'ATVG'),
        (Diger, 'DİĞER KAMU KURUM KURULUŞLARINA AİT YAPILAR'),

    )

    Diger = (

        (Hukumet_konagi_icinde, 'HÜKÜMET KONAĞI İÇİNDE'),
        (Hukumet_konagi_ayri, 'HÜKÜMET KONAĞINDA AYRI BLOK'),
        (Diger, 'DİĞER KAMU KURUM KURULUŞLARINA AİT YAPILAR'),

    )
    adaletYapisi = 'ADALET YAPILARI'
    kiraliktasinmaz = 'KİRALIK TAŞINMAZLAR'
    tahisisliArsalar = 'TAHSİSLİ ARSALAR'
    lojmanlar = 'LOJMANLAR'
    cezaInfazKurumlari = 'CEZA İNFAZ KURUMLARI'

    TasinmazType = (
        (adaletYapisi, 'ADALET YAPILARI'),
        (kiraliktasinmaz, 'KİRALIK TAŞINMAZLAR'),
        (tahisisliArsalar, 'TAHSİSLİ ARSALAR'),
        (lojmanlar, 'LOJMANLAR'),
        (cezaInfazKurumlari, 'CEZA İNFAZ KURUMLARI'),
    )
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

    TAHSIS_AMACI = (
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

    name = models.CharField(max_length=120, null=True, blank=True)
    sirano = models.IntegerField(blank=True, null=True, )
    tkgmno = models.IntegerField(blank=True, null=True, )
    tapu = models.ForeignKey(GTapu, on_delete=models.SET_NULL, verbose_name='Tapu', null=True, blank=True)
    kurum = models.ManyToManyField(Gkurum)

    mustakil = models.CharField(max_length=128, verbose_name='müstakil ', choices=Mustakil, default=Hazine)
    diger = models.CharField(max_length=128, verbose_name='digermulkiyet ', choices=Diger,
                             default=Hukumet_konagi_icinde)

    tahsisAmaci = models.CharField(max_length=128, verbose_name='Tasinmazin Türü ', choices=TAHSIS_AMACI,
                                   default=AB)
    tasinmazinTuru = models.CharField(max_length=128, verbose_name='Tasinmazin Türü ', choices=TasinmazType,
                                      default=adaletYapisi)

    kira = models.ForeignKey(Gkira, on_delete=models.SET_NULL, verbose_name='Kurum', null=True, blank=True)
    tahsis = models.ForeignKey(Gtahsis, on_delete=models.SET_NULL, verbose_name='Tahsis', null=True, blank=True)
    definition = models.CharField(max_length=128, verbose_name='Tasınmaz Açıklama ', null=True, blank=True)

    offers = models.ManyToManyField(EPOffer)
    documents = models.ManyToManyField(GtasinmazDocument)


    arsaDegeri = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    yapiMalitet = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    yapiRaic = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    # adalet yapı detayi
    yapimyili = models.DateTimeField(null=True, blank=True)
    edinimyili = models.DateTimeField(null=True, blank=True)
    blokadeti = models.IntegerField(null=True, blank=True)
    katadedi = models.IntegerField(null=True, blank=True)
    kapalikullanimalani = models.IntegerField(null=True, blank=True)
    binaAltTur = models.ForeignKey(GtasinmazAltTur, on_delete=models.SET_NULL, verbose_name='binaalttur', blank=True,
                                   null=True)
    binaustTur = models.ForeignKey(GtasinmazUstTur, on_delete=models.SET_NULL, verbose_name='binaüsttur', blank=True,
                                   null=True)



    kobilid = models.IntegerField(null=True, blank=True, default=2)
