from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from oxiterp.settings.base import MEDIA_URL
from sbs.Forms.GkiraForm import GkiraForm
from sbs.Forms.GtahsisForm import GtahsisForm
from sbs.Forms.GtasinmazForm import GtasinmazForm
from sbs.Forms.GteskilatForm import GteskilatForm
from sbs.Forms.KurumForm import KurumForm
from sbs.Forms.TapuForm import TapuForm
from sbs.models.GTapu import GTapu
from sbs.models.Gkira import Gkira
from sbs.models.Gkurum import Gkurum
from sbs.models.Gtahsis import Gtahsis
from sbs.models.Gtasinmaz import Gtasinmaz
from sbs.models.Gteskilat import Gteskilat
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
    user = request.user
    project_form = GtasinmazForm(request.POST or None, instance=tasinmaz)

    if tasinmaz.teskilat == None:
        teskilat = Gteskilat()
        teskilat.save()
        tasinmaz.teskilat = teskilat
        tasinmaz.save()
        teskilat_form = GteskilatForm(request.POST or None, instance=teskilat)
    else:
        teskilat_form = GteskilatForm(request.POST or None, instance=tasinmaz.teskilat)

    if tasinmaz.tapu == None:
        tapu = GTapu()
        tapu.save()
        tasinmaz.tapu = tapu
        tasinmaz.save()
        tapu_form = TapuForm(request.POST or None, instance=tapu)
    else:
        tapu_form = TapuForm(request.POST or None, instance=tasinmaz.tapu)

    if tasinmaz.tahsis_durumu == Gtasinmaz.Arsa:
        if tasinmaz.tahsis == None:
            tahsis = Gtahsis()
            tahsis.save()
            tasinmaz.tahsis = tahsis
            tasinmaz.save()
        else:
            tahsis = tasinmaz.tahsis
        tahsis_form = GtahsisForm(request.POST or None, instance=tahsis)

    elif tasinmaz.tahsis_durumu == Gtasinmaz.Kira:
        if tasinmaz.kira == None:
            kira = Gkira()
            kira.save()
            tasinmaz.kira = kira
            tasinmaz.save()
        else:
            kira = tasinmaz.kira
        tahsis_form = GkiraForm(request.POST or None, instance=kira)
    else:
        tahsis_form = GkiraForm()

    if request.method == 'POST':
        if project_form.is_valid() and tahsis_form.is_valid() and tapu_form.is_valid():
            projectSave = project_form.save()
            tahsis = tahsis_form.save()
            tapu = tapu_form.save()
            log = str(tasinmaz.name) + "tasinmaz  güncelledi"
            log = general_methods.logwrite(request, log)

            messages.success(request, 'Tasinmaz Başarıyla Güncellendi')
            return redirect('sbs:tasinmaz-duzenle', pk=tasinmaz.pk)
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')
    return render(request, 'tasinmaz/tasinmazGuncelle.html',
                  {'project_form': project_form,
                   'project': tasinmaz, 'tahsis_form': tahsis_form, 'tapu_form': tapu_form,
                   'teskilat_form': teskilat_form})


@login_required
def tasinmaz_list(request):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    projects = Gtasinmaz.objects.all()
    user = request.user

    return render(request, 'tasinmaz/tasinmazlar.html', {'projects': projects})


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
        except EPProject.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def add_kurum(request):
    perm = general_methods.control_access_personel(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    kurum_form = KurumForm(request.POST or None)
    if request.method == 'POST':
        if kurum_form.is_valid():
            kurum = kurum_form.save(commit=False)
            kurum.save()
            return redirect('sbs:kurum-duzenle', kurum.pk)
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kurum/kurumEkle.html', {'kurum_form': kurum_form})


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

    return render(request, 'kurum/KurumGuncelle.html', {'kurum': kurum, 'kurum_form': kurum_form})
