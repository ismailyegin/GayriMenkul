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
    TahsisliArsa = "Tahsisli"
    Kira = "Kiralık"

    TahsisDurumu = (

        (TahsisliArsa, 'Tahsisli'),
        (Kira, 'Kiralık'),
    )

    Konut = "Konut"
    Misafirhane = "Misafirhane"

    lojmanTuru = (

        (Konut, 'Konut'),
        (Misafirhane, 'Misafirhane'),
    )

    Bina = "Bina"
    Arsa = "Arsa"

    ArsaDurumu = (

        (Bina, 'Bina'),
        (Arsa, 'Arsa'),
    )

    IsFormal = (
        (True, 'Evet '),
        (False, 'Hayır'),
    )

    ArsaDurumu = (

        (Bina, 'Bina'),
        (Arsa, 'Arsa'),
    )

    fall = "Faal"
    Atıl = "Atıl veya Metrut"
    yikik = 'Yıkık'

    lojmanKullanimTuru = (

        (fall, 'Faal'),
        (Atıl, 'Atıl veya Metrut'),
        (yikik, 'Yıkık'),
    )



    Hazine = 'HAZİNE'
    Hukumet_konagi_icinde = "HÜKÜMET KONAGI İÇERİSİNDE"
    Hukumet_konagi_ayri = "HÜKÜMET KONAGI AYRİ BLOK"
    Is_yurtlari = "İŞ YURTLARI"
    Diger = "DİĞER KAMU KURUM KURULUŞLARINDAN TAHSİSLİ "
    Atvg = 'ATGV'
    Kiralik = "KİRALIK"
    belediye = 'BELEDİYE'
    bos = None

    Mustakil = (
        (bos, 'Seçiniz'),
        (belediye, 'BELEDİYE'),
        (Hazine, 'HAZİNE'),
        (Is_yurtlari, 'İŞ YURTLARI'),
        (Atvg, 'ATGV'),
        (Diger, 'DİĞER KAMU KURUM KURULUŞLARINA AİT YAPILAR'),


    )

    Diger = (


        (Hukumet_konagi_icinde, 'HÜKÜMET KONAĞI İÇİNDE'),
        (Hukumet_konagi_ayri, 'HÜKÜMET KONAĞINDA AYRI BLOK'),
        (Diger, 'DİĞER KAMU KURUM KURULUŞLARINA AİT YAPILAR'),
        (bos, 'Seçiniz'),

    )
    adaletYapisi = 'ADALET BİNASI'
    # kiraliktasinmaz = 'KİRALIK TAŞINMAZLAR'
    tahisisliArsalar = 'ARSA'
    lojmanlar = 'LOJMAN'
    cezaInfazKurumlari = 'CEZA İNFAZ KURUMU'
    adlitip = 'ADLİ TIP'
    egitimMerkezi = 'EGİTİM MERKEZİ'
    denetimli = 'DENETİMLİ SERBESTLİK'
    sosyal = 'SOSYAL TESİS'


    TasinmazType = (
        (adaletYapisi, 'ADALET BİNASI'),
        # (kiraliktasinmaz, 'KİRALIK TAŞINMAZLAR'),
        (tahisisliArsalar, 'ARSA'),
        (lojmanlar, 'LOJMAN'),
        (adlitip, 'ADLİ TIP'),
        (egitimMerkezi, 'EGİTİM MERKEZİ'),
        (denetimli, 'DENETİMLİ SERBESTLİK'),
        (sosyal, 'SOSYAL TESİS'),
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

    mustakil = models.CharField(max_length=128, verbose_name='müstakil ', choices=Mustakil, default=bos, null=True,
                                blank=True)
    diger = models.CharField(max_length=128, verbose_name='digermulkiyet ', choices=Diger, default=bos, null=True,
                             blank=True)

    tahsisAmaci = models.CharField(max_length=128, verbose_name='Tasinmazin Türü ', choices=TAHSIS_AMACI,
                                   default=AB)
    tasinmazinTuru = models.CharField(max_length=128, verbose_name='Tasinmazin Türü ', choices=TasinmazType, null=True,
                                      blank=True)


    definition = models.CharField(max_length=128, verbose_name='Tasınmaz Açıklama ', null=True, blank=True)

    offers = models.ManyToManyField(EPOffer)
    documents = models.ManyToManyField(GtasinmazDocument)

    arsaDegeri = models.IntegerField(blank=True, null=True, )
    yapiMalitet = models.IntegerField(blank=True, null=True, )
    yapiRaic = models.IntegerField(blank=True, null=True, )

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
    # tahsisli arsa
    tahsisDurumu = models.CharField(max_length=128, verbose_name='tahsis durumu ', choices=TahsisDurumu, blank=True,
                                    null=True)
    kira = models.ForeignKey(Gkira, on_delete=models.SET_NULL, verbose_name='kira', null=True, blank=True)
    tahsis = models.ForeignKey(Gtahsis, on_delete=models.SET_NULL, verbose_name='Tahsis', null=True, blank=True)

    # lojman

    blockSayisi = models.IntegerField(blank=True, null=True, )
    daireSayisi = models.IntegerField(blank=True, null=True, )
    lojmanYapimYili = models.DateTimeField(null=True, blank=True)
    lojmanturu = models.CharField(max_length=128, verbose_name='lojman_turu ', choices=lojmanTuru, default=Konut)
    daireAlaniNet = models.IntegerField(blank=True, null=True, )
    daireBrut = models.IntegerField(blank=True, null=True, )
    lojmanKullanim = models.CharField(max_length=128, verbose_name='lojman_kullanim_turu',
                                      choices=lojmanKullanimTuru, default=fall, null=True
                                      )

    hDaireSayisi = models.IntegerField(blank=True, null=True, )
    atvgdaireSayisi = models.IntegerField(blank=True, null=True, )
    isDaireSayisi = models.IntegerField(blank=True, null=True, )
    mDaireSayisi = models.IntegerField(blank=True, null=True, )
    mSavciSayisi = models.IntegerField(blank=True, null=True, )
    mAyriBlock = models.BooleanField(default=True, choices=IsFormal)
    blockDaire = models.IntegerField(blank=True, null=True, )

    # lojmanturu = models.CharField(max_length=128, verbose_name='lojman_turu ', choices=lojmanTuru, default=Konut)
    # daireKapaliKulllanimAlaniNet = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    # daireKapaliKulllanimAlaniBrut = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    # lojmanKullanimDurumu = models.CharField(max_length=128, verbose_name='lojman_kullanim_turu',
    #                                         choices=lojmanKullanimTuru, default=fall)
    #
    # hazinelojmaniDaireSayisi = models.IntegerField(blank=True, null=True, )
    # atvglojmaniDaireSayisi = models.IntegerField(blank=True, null=True, )
    # isyurtlariDaireSayisi = models.IntegerField(blank=True, null=True, )
    # mahaldekiToplamDaireSayisi = models.IntegerField(blank=True, null=True, )
    # mahaldekiToplamHakimSavcıSayisi = models.IntegerField(blank=True, null=True, )
    # arsayuzolcumu = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    # mustakilAyriBlock = models.BooleanField(default=True, choices=IsFormal)
    # blockicindeDaire = models.IntegerField(blank=True, null=True, )



    # ceza infaz kurumlari

    tipi = models.CharField(max_length=128, verbose_name='tipi ', null=True, blank=True)
    kapasitesi = models.IntegerField(blank=True, null=True, )
    brutKapaliAlan = models.IntegerField(blank=True, null=True, )




    kobilid = models.IntegerField(null=True, blank=True, default=2)
