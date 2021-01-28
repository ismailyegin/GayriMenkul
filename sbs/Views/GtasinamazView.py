from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from sbs.Forms.GtasinmazForm import GtasinmazForm
from sbs.models.Gtasinmaz import Gtasinmaz
from sbs.services import general_methods


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
    project = Gtasinmaz.objects.get(pk=pk)
    user = request.user

    project_form = GtasinmazForm(request.POST or None, instance=project)

    if request.method == 'POST':
        if project_form.is_valid():
            projectSave = project_form.save()
            log = str(project.name) + "tasinmaz  güncelledi"
            log = general_methods.logwrite(request, log)

            messages.success(request, 'Tasinmaz Başarıyla Güncellendi')
            return redirect('sbs:tasinmaz-duzenle', pk=project.pk)
        else:
            messages.warning(request, 'Alanları Kontrol Ediniz')
    return render(request, 'tasinmaz/tasinmazGuncelle.html',
                  {'project_form': project_form,
                   'project': project, })


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
