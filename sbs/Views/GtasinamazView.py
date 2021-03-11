from builtins import print
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render

from oxiterp.settings.base import MEDIA_URL
from sbs.Forms.GBolgeForm import GbolgeForm
from sbs.Forms.GkiraForm import GkiraForm
from sbs.Forms.GtahsisForm import GtahsisForm
#   adalet alanina göre form üretimi oldu
from sbs.Forms.GtasinmazAdliyeForm import GtasinmazAdliyeForm
from sbs.Forms.GtasinmazArsaForm import GtasinmazArsaForm
from sbs.Forms.GtasinmazForm import GtasinmazForm
from sbs.Forms.GtasinmazSearchForm import GtasinmazSearchForm
from sbs.Forms.GtasinmazcezainfazForm import GtasinmazcezainfazForm
from sbs.Forms.GtasinmazlojmanForm import GtasinmazlojmanForm
from sbs.Forms.GteskilatForm import GteskilatForm
from sbs.Forms.GteskilatSearchForm import GteskilatSearchForm
from sbs.Forms.KurumForm import KurumForm
from sbs.Forms.TapuForm import TapuForm
from sbs.models import City
from sbs.models.GTapu import GTapu
from sbs.models.Gbolge import Gbolge
from sbs.models.Gkira import Gkira
from sbs.models.Gkurum import Gkurum
from sbs.models.Gtahsis import Gtahsis
from sbs.models.Gtasinmaz import Gtasinmaz
from sbs.models.GtasinmazBinaAltTur import GtasinmazAltTur
from sbs.models.GtasinmazDocument import GtasinmazDocument
from sbs.models.Gteskilat import Gteskilat
from sbs.models.Town import Town
from sbs.services import general_methods
from sbs.services.general_methods import getProfileImage


# from twisted.conch.insults.insults import privateModes
@login_required
def add_tasinmaz(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    project_form = GtasinmazForm()

    if request.method == 'POST':
        project_form = GtasinmazForm(request.POST)
        if project_form.is_valid():
            project = project_form.save()
            log = str(project.name) + " tasınmaz  kaydetti"
            log = general_methods.logwrite(request, log)

            messages.success(request, 'Tasınmaz  Kaydedilmiştir.')

            return redirect('sbs:tasinmaz-duzenle', pk=project.pk)

        else:
            messages.warning(request, 'Alanları kontrol ediniz.')
    return render(request, 'tasinmaz/tasinmazEkle.html',
                  {'project_form': project_form})


@login_required
def edit_tasinmaz(request, pk):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    tasinmaz = Gtasinmaz.objects.get(pk=pk)
    if tasinmaz.tapu == None:
        tapu = GTapu()
        tapu.save()
        tasinmaz.tapu = tapu
        tasinmaz.save()
    print(tasinmaz.tasinmazinTuru)

    if tasinmaz.tasinmazinTuru == tasinmaz.adaletYapisi:
        project_form = GtasinmazAdliyeForm(request.POST or None, instance=tasinmaz)
        gkurum = Gkurum.objects.all()
        tapu_form = TapuForm(request.POST, instance=tasinmaz.tapu)
        if not (tasinmaz.tahsis):
            tahsis = Gtahsis()
            tahsis.save()
            tasinmaz.tahsis = tahsis
            tasinmaz.save()

        if not (tasinmaz.kira):
            kira = Gkira()
            kira.save()
            tasinmaz.kira = kira
            tasinmaz.save()
        kiralik_form = GkiraForm(request.POST, instance=tasinmaz.kira)
        tahsis_form = GtahsisForm(request.POST, instance=tasinmaz.tahsis)

        if request.method == 'POST':

            if request.FILES.get('file'):
                document = GtasinmazDocument(name=request.FILES.get('file'))
                document.save()
                tasinmaz.documents.add(document)
                tasinmaz.save()

            if project_form.is_valid() and tapu_form.is_valid():
                projectSave = project_form.save(commit=False)
                projectSave.save()
                tapu_form.save()
                log = str(tasinmaz.name) + "tasinmaz  güncelledi"
                log = general_methods.logwrite(request, log)
                print('log')
            else:
                print('alanlari kontrol ediniz')
                messages.warning(request, 'Alanlari kontrol ediniz')
            # kaydetme testi yapılacak
            if kiralik_form.is_valid():
                kiralik_form.save()

            if tahsis_form.is_valid():
                tahsis_form.save()
            return redirect('sbs:tasinmaz-duzenle', pk=projectSave.pk)



        if tasinmaz.binaustTur:
            if tasinmaz.binaAltTur:
                project_form.fields['binaAltTur'].queryset = GtasinmazAltTur.objects.filter(ust=tasinmaz.binaustTur)
                project_form.fields['binaAltTur'].initial = tasinmaz.binaAltTur
            else:
                project_form.fields['binaAltTur'].queryset = GtasinmazAltTur.objects.filter(ust=tasinmaz.binaustTur)
        else:
            project_form.fields['binaAltTur'].queryset = GtasinmazAltTur.objects.none()

        if tasinmaz.tapu.city:
            if tasinmaz.tapu.town:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
                tapu_form.fields['town'].initial = tasinmaz.tapu.town.name
            else:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
        else:
            tapu_form.fields['town'].queryset = Town.objects.none()
        return render(request, 'tasinmaz/tasinmazAdliyeGuncelle.html',
                      {'project_form': project_form,
                       'project': tasinmaz,
                       'tapu_form': tapu_form,
                       'gkurum': gkurum,
                       'tahsis_form': tahsis_form,
                       'kiralik_form': kiralik_form,
                       })

    elif tasinmaz.tasinmazinTuru == tasinmaz.tahisisliArsalar:
        project_form = GtasinmazArsaForm(request.POST or None, instance=tasinmaz)
        tapu_form = TapuForm(request.POST, instance=tasinmaz.tapu)

        if not (tasinmaz.tahsis):
            tahsis = Gtahsis()
            tahsis.save()
            tasinmaz.tahsis = tahsis
            tasinmaz.save()

        tahsis_form = GtahsisForm(request.POST or None, instance=tasinmaz.tahsis)

        if request.method == 'POST':

            if request.FILES.get('file'):
                document = GtasinmazDocument(name=request.FILES.get('file'))
                document.save()
                tasinmaz.documents.add(document)
                tasinmaz.save()

            if project_form.is_valid() and tapu_form.is_valid():
                projectSave = project_form.save(commit=False)
                projectSave.save()
                tapu_form.save()
                log = str(tasinmaz.name) + "tasinmaz  güncelledi"
                log = general_methods.logwrite(request, log)
                print('log arsa ')
                return redirect('sbs:tasinmaz-duzenle', pk=projectSave.pk)
            else:
                print('alanlari kontrol ediniz arsa')
                messages.warning(request, 'Alanlari kontrol ediniz')
        if tasinmaz.tapu.city:
            if tasinmaz.tapu.town:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
                tapu_form.fields['town'].initial = tasinmaz.tapu.town.name
            else:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
        else:
            tapu_form.fields['town'].queryset = Town.objects.none()

        project_form.fields['tahsisDurumu'].queryset = None
        project_form.fields['tahsisDurumu'].initial = tasinmaz.TahsisliArsa



        return render(request, 'tasinmaz/tasinmaztahsisliArsaGuncelle.html',
                      {
                          'project_form': project_form,
                          'tapu_form': tapu_form,
                          'tahsis_form': tahsis_form


                      })
    elif tasinmaz.tasinmazinTuru == tasinmaz.lojmanlar:

        project_form = GtasinmazlojmanForm(request.POST or None, instance=tasinmaz)
        tapu_form = TapuForm(request.POST, instance=tasinmaz.tapu)
        if not (tasinmaz.tahsis):
            tahsis = Gtahsis()
            tahsis.save()
            tasinmaz.tahsis = tahsis
            tasinmaz.save()

        if not (tasinmaz.kira):
            kira = Gkira()
            kira.save()
            tasinmaz.kira = kira
            tasinmaz.save()
        kiralik_form = GkiraForm(request.POST, instance=tasinmaz.kira)
        tahsis_form = GtahsisForm(request.POST, instance=tasinmaz.tahsis)
        if request.method == 'POST':

            if request.FILES.get('file'):
                document = GtasinmazDocument(name=request.FILES.get('file'))
                document.save()
                tasinmaz.documents.add(document)
                tasinmaz.save()
            if kiralik_form.is_valid():
                kiralik_form.save()

            if tahsis_form.is_valid():
                tahsis_form.save()

            if project_form.is_valid() and tapu_form.is_valid():
                projectSave = project_form.save(commit=False)
                projectSave.save()
                tapu_form.save()
                log = str(tasinmaz.name) + "tasinmaz  güncelledi"
                log = general_methods.logwrite(request, log)
                print('log lojman ')


            else:
                print('alanlari kontrol ediniz lojman')
                messages.warning(request, 'Alanlari kontrol ediniz')
            return redirect('sbs:tasinmaz-duzenle', pk=projectSave.pk)

        if tasinmaz.tapu.city:
            if tasinmaz.tapu.town:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
                tapu_form.fields['town'].initial = tasinmaz.tapu.town.name
            else:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
        else:
            tapu_form.fields['town'].queryset = Town.objects.none()

        return render(request, 'tasinmaz/TasinmazLojmanGuncelle.html',
                      {
                          'project_form': project_form,
                          'tapu_form': tapu_form,
                          'tahsis_form': tahsis_form,
                          'kiralik_form': kiralik_form,
                      })


    elif tasinmaz.tasinmazinTuru == tasinmaz.cezaInfazKurumlari:
        project_form = GtasinmazcezainfazForm(request.POST or None, instance=tasinmaz)
        tapu_form = TapuForm(request.POST, instance=tasinmaz.tapu)
        if not (tasinmaz.tahsis):
            tahsis = Gtahsis()
            tahsis.save()
            tasinmaz.tahsis = tahsis
            tasinmaz.save()

        if not (tasinmaz.kira):
            kira = Gkira()
            kira.save()
            tasinmaz.kira = kira
            tasinmaz.save()
        kiralik_form = GkiraForm(request.POST, instance=tasinmaz.kira)
        tahsis_form = GtahsisForm(request.POST, instance=tasinmaz.tahsis)
        if request.method == 'POST':

            if request.FILES.get('file'):
                document = GtasinmazDocument(name=request.FILES.get('file'))
                document.save()
                tasinmaz.documents.add(document)
                tasinmaz.save()
            if kiralik_form.is_valid():
                kiralik_form.save()

            if tahsis_form.is_valid():
                tahsis_form.save()

            if project_form.is_valid() and tapu_form.is_valid():
                projectSave = project_form.save(commit=False)
                projectSave.save()
                tapu_form.save()
                log = str(tasinmaz.name) + "tasinmaz  güncelledi"
                log = general_methods.logwrite(request, log)
                print('log ceza ')
                return redirect('sbs:tasinmaz-duzenle', pk=projectSave.pk)


            else:
                print('alanlari kontrol ediniz ceza')
                messages.warning(request, 'Alanlari kontrol ediniz')

        if tasinmaz.tapu.city:
            if tasinmaz.tapu.town:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
                tapu_form.fields['town'].initial = tasinmaz.tapu.town.name
            else:
                tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
        else:
            tapu_form.fields['town'].queryset = Town.objects.none()

        return render(request, 'tasinmaz/tasinmazCezaInfazGuncellle.html',
                      {
                          'project_form': project_form,
                          'tapu_form': tapu_form,
                          'kiralik_form': kiralik_form,
                          'tahsis_form': tahsis_form,
                      })
    else:
        return redirect('sbs:tasinmaz-list')

    # if tasinmaz.tapu.city:
    #     if tasinmaz.tapu.town:
    #         tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
    #         tapu_form.fields['town'].initial = tasinmaz.tapu.town
    #     else:
    #         tapu_form.fields['town'].queryset = Town.objects.filter(cityId=tasinmaz.tapu.city.pk)
    # else:
    #     tapu_form.fields['town'].queryset = Town.objects.none()

    # if tasinmaz.tahsis == None:
    #     tahsis = Gtahsis()
    #     tahsis.save()
    #     tasinmaz.tahsis = tahsis
    #     tasinmaz.save()
    # else:
    #     tahsis = tasinmaz.tahsis
    # tahsis_form = GtahsisForm(request.POST or None, instance=tahsis)
    #
    # if tasinmaz.kira == None:
    #     kira = Gkira()
    #     kira.save()
    #     tasinmaz.kira = kira
    #     tasinmaz.save()
    # else:
    #     kira = tasinmaz.kira
    # kira_form = GkiraForm(request.POST or None, instance=kira)





@login_required
def tasinmaz_list(request):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    projects = Gtasinmaz.objects.none()
    tasinmaz_form = GtasinmazSearchForm()

    if request.method == 'POST':
        name = request.POST.get('name')
        sirano = request.POST.get('sirano')
        tkgmno = request.POST.get('tkgmno')
        mulkiyet = request.POST.get('mulkiyet')
        tahsis_durumu = request.POST.get('tahsis_durumu')
        arsaTuru = request.POST.get('arsaTuru')

        if not (name or sirano or tkgmno or mulkiyet or tahsis_durumu or arsaTuru):
            projects = Gtasinmaz.objects.all()
        else:
            query = Q()
            if name:
                query &= Q(name__icontains=name)
            if sirano:
                query &= Q(sirano=sirano)
            if tkgmno:
                query &= Q(tkgmno=tkgmno)
            if mulkiyet:
                query &= Q(mulkiyet=mulkiyet)
            if tahsis_durumu:
                query &= Q(tahsis_durumu=tahsis_durumu)
            if arsaTuru:
                query &= Q(arsaTuru=arsaTuru)

            if request.user.groups.filter(name__in=['Yonetim', 'Admin']):
                projects = Gtasinmaz.objects.filter(query).distinct()


    return render(request, 'tasinmaz/tasinmazlar.html', {'projects': projects,
                                                         'tasinmaz_form': tasinmaz_form})


@login_required
def delete_tasinmaz(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Gtasinmaz.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def add_offer_to_project(request, pk):
    perm = general_methods.control_access_personel(request)

    print('geldim')

    if not perm:
        logout(request)
        return redirect('accounts:login')

    message = request.POST.get('message')
    project = Gtasinmaz.objects.get(pk=pk)
    username = request.user.first_name + " " + request.user.last_name
    person = getProfileImage(request)
    imageUrl = MEDIA_URL + "profile/logo.png"
    date = datetime.now()
    dates = date.strftime('%d/%m/%Y %H:%M')

    log = str(project.name) + " tasinmazina  yeni bir görüs ekledi time=" + str(dates)
    log = general_methods.logwrite(request, log)

    project.offers.create(message=message, added_by=request.user)

    # for item in project.employees.all().exclude(employee__user=request.user):
    #     notification = Notification(notification=project.name +" Projesine yeni bir görüs eklendi.",
    #                                 users=item.employee.user,
    #                                 entityId=project.pk,
    #                                 tableName="proje"
    #                                 )
    #     notification.save()
    #
    #
    #

    try:
        print()

        return JsonResponse({'status': 'Success', 'username': username, 'image': imageUrl, 'dates': dates})
    except:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})

    return redirect('sbs:proje-duzenle', pk=pk)


@login_required
def delete_ofters_from_project(request, project_pk, employee_pk):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        try:
            athlete = Gtasinmaz.objects.get(pk=project_pk)
            athlete.offers.remove(employee_pk)
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def add_kurum(request):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    if request.method == 'POST':
        kurum_form = KurumForm(request.POST or None)
        if kurum_form.is_valid():
            kurum = kurum_form.save(commit=False)
            kurum.save()
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')
    kurum = Gkurum.objects.all()
    kurum_form = KurumForm()

    return render(request, 'kurum/kurumEkle.html', {'kurum_form': kurum_form, 'kurum': kurum})


@login_required
def edit_kurum(request, pk):
    perm = general_methods.control_access_personel(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    kurum = Gkurum.objects.get(pk=pk)
    kurum_form = KurumForm(request.POST or None, instance=kurum)
    kurum = Gkurum.objects.all()
    if request.method == 'POST':
        if kurum_form.is_valid():
            kurum_form.save()
            return redirect('sbs:kurum-add', )


    return render(request, 'kurum/KurumGuncelle.html', {'kurum': kurum, 'kurum_form': kurum_form})


@login_required
def add_teskilat(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    teskilat_form = GteskilatForm()
    if request.method == 'POST':
        teskilat_form = GteskilatForm(request.POST)
        if teskilat_form.is_valid():
            project = teskilat_form.save()
            log = str(project.city) + " teşkilat yapısı kaydedildi"
            log = general_methods.logwrite(request, log)
            messages.success(request, 'Teşkilat Yapısı Kaydedildi.  Kaydedilmiştir.')

            return redirect('sbs:teskilat-duzenle', pk=project.pk)
        else:
            messages.warning(request, 'Alanları kontrol ediniz.')
    return render(request, 'teskilat/teskilatEkle.html',
                  {'project_form': teskilat_form})


def list_teskilat(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    teskilat = Gteskilat.objects.none()
    teskilat_form = GteskilatSearchForm()
    if request.method == 'POST':
        tasinmaz_form = GteskilatSearchForm(request.POST)
        if tasinmaz_form.is_valid():
            depremderecesi = tasinmaz_form.cleaned_data.get('depremderecesi')
            city = tasinmaz_form.cleaned_data.get('city')
            yargiBolgesi = tasinmaz_form.cleaned_data.get('yargiBolgesi')
            town = tasinmaz_form.cleaned_data.get('town')

            if not (depremderecesi or city or yargiBolgesi or town):
                teskilat = Gteskilat.objects.all()
            else:
                query = Q()
                if depremderecesi:
                    query &= Q(depremderecesi=depremderecesi)
                if city:
                    query &= Q(city=city)
                if yargiBolgesi:
                    query &= Q(yargiBolgesi=yargiBolgesi)
                if town:
                    query &= Q(town=town)

                if request.user.groups.filter(name__in=['Yonetim', 'Admin']):
                    teskilat = Gteskilat.objects.filter(query).distinct()

    return render(request, 'teskilat/teskilatlar.html',
                  {'teskilat': teskilat, 'teskilat_form': teskilat_form})
@login_required
def edit_teskilat(request, pk):
    perm = general_methods.control_access_personel(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')
    teskilat = Gteskilat.objects.get(pk=pk)
    teskilat_form = GteskilatForm(request.POST or None, instance=teskilat)
    if teskilat.acm:
        teskilat_form.fields['acm'].queryset = Gbolge.objects.filter(type=Gbolge.Acm)
        teskilat_form.fields['acm'].initial = teskilat.acm.name
    else:
        teskilat_form.fields['acm'].queryset = Gbolge.objects.filter(type=Gbolge.Acm)
    if teskilat.bim:
        teskilat_form.fields['bim'].queryset = Gbolge.objects.filter(type=Gbolge.Bim)
        teskilat_form.fields['bim'].initial = teskilat.bim.name
    else:
        teskilat_form.fields['bim'].queryset = Gbolge.objects.filter(type=Gbolge.Bim)
    if teskilat.bam:
        teskilat_form.fields['bam'].queryset = Gbolge.objects.filter(type=Gbolge.Bam)
        teskilat_form.fields['bam'].initial = teskilat.bam.name
    else:
        teskilat_form.fields['bam'].queryset = Gbolge.objects.filter(type=Gbolge.Bam)
    if request.method == 'POST':
        if teskilat_form.is_valid():
            teskilat_form.save()
            log = str(teskilat.city) + " teşkilat yapısı güncellendi."
            log = general_methods.logwrite(request, log)
            messages.success(request, 'Teşkilat Yapısı güncellendi.')

        else:
            messages.warning(request, 'Alanları kontrol ediniz.')
    return render(request, 'teskilat/teskilatGuncelle.html',
                  {'project_form': teskilat_form,
                   })
@login_required
def add_teskilat_olustur(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    cities = City.objects.all()
    for item in cities:
        if not (Gteskilat.objects.filter(city=item)):
            teskilat = Gteskilat(city=item)
            teskilat.save()
    return render(request, 'tasinmaz/tasinmazEkle.html')


@login_required
def project_subfirma(request, pk):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    try:
        tasinmaz = Gtasinmaz.objects.get(pk=pk)
        if request.POST.get('title'):
            birim = Gkurum.objects.get(pk=request.POST.get('title'))
            tasinmaz.kurum.add(birim)
            tasinmaz.save()
            log = str(tasinmaz.name) + " tasinmaz kullanan birim eklendi" + str(birim.name)
            log = general_methods.logwrite(request, log)
        return JsonResponse({'status': 'Success', 'messages': 'save successfully', 'pk': birim.pk})

    except:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})
        messages.warning(request, 'Yeniden deneyiniz.')

    return redirect('sbs:tasinmaz-duzenle', pk=pk)


@login_required
def delete_birim_tasinmaz(request, tasinmaz, kurum):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.method == 'POST' and request.is_ajax():
        tasinmaz = Gtasinmaz.objects.get(pk=tasinmaz)
        kurum = Gkurum.objects.get(pk=kurum)
        tasinmaz.kurum.remove(kurum)
        tasinmaz.save()
        try:
            # tasinmaz = Gtasinmaz.objects.get(pk=tasinmaz)
            # kurum=Gkurum.objects.get(pk=kurum)
            # tasinmaz.kurum.remove(kurum)
            # tasinmaz.save()
            print()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def tasimazAltTur(request):
    perm = general_methods.control_access_personel(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    try:
        if request.method == 'POST':
            project = GtasinmazAltTur.objects.filter(ust__name=request.POST.get('cmd'))
            beka = []
            for item in project:
                data = {
                    'pk': item.pk,
                    'name': item.name,
                }
                beka.append(data)
            return JsonResponse(
                {
                    'data': beka,
                    'msg': 'Valid is  request'
                })

    except:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def BolgeAdd(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    if request.method == 'POST':
        project_form = GbolgeForm(request.POST)
        if project_form.is_valid():
            project_form.save()
        else:
            print('alanlari kontrol ediniz')
    project_form = GbolgeForm()
    regions = Gbolge.objects.all()

    project_form.fields['town'].queryset = Town.objects.none()
    return render(request, 'Bolge/BolgeEkle.html', {
        'regions': regions,
        'project_form': project_form
    })


@login_required
def bolgeUpdate(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    region = Gbolge.objects.get(pk=pk)
    project_form = GbolgeForm(request.POST or None, instance=region)

    if request.method == 'POST':
        if project_form.is_valid():
            project_form.save()
            return redirect('sbs:bolge-ekle')
    if region.town:
        project_form.fields['town'].queryset = Town.objects.filter(cityId=region.city.pk)
        project_form.fields['town'].initial = region.name
    else:
        project_form.fields['town'].queryset = Town.objects.filter(cityId=region.city.pk)

    return render(request, 'Bolge/BolgeGuncelle.html', {
        'project_form': project_form
    })
