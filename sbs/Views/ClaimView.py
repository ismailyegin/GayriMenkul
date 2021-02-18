from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sbs.Forms.ClaimForm import ClaimForm
from sbs.models import MenuDirectory, MenuAdmin
from sbs.models.Claim import Claim
from sbs.services import general_methods


@login_required
def return_claim(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    destek = Claim.objects.filter(kobilid=2).order_by('-creationDate')

    return render(request, 'Destek/DestekTalepListesi.html', {'claims': destek})


@login_required
def claim_add(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    claim_form = ClaimForm()

    if request.method == 'POST':
        claim_form = ClaimForm(request.POST)
        if claim_form.is_valid():
            claim_form.save()

            messages.success(request, 'Destek Talep  Eklendi.')
            return redirect('sbs:destek-talep-listesi')

    return render(request, 'Destek/Desktek-ekle.html', {'claim_form': claim_form, })


@login_required
def claim_update(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    clain = Claim.objects.get(pk=pk)
    claim_form = ClaimForm(request.POST or None, instance=clain)

    if request.method == 'POST':
        if claim_form.is_valid():
            claim_form.save()
            messages.success(request, 'Destek Talep  Güncellendi.')
            return redirect('sbs:destek-talep-listesi')

    return render(request, 'Destek/Desktek-ekle.html', {'claim_form': claim_form, })


@login_required
def claim_delete(request, pk):
    perm = general_methods.control_access(request)
    if not perm:
        logout(request)
        return redirect('accounts:login')

    clain = Claim.objects.get(pk=pk)
    clain.delete()

    messages.success(request, 'Destek Talep  Silindi.')

    return redirect('sbs:destek-talep-listesi')


@login_required
def menu(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    admin = MenuAdmin.objects.all()
    for m in admin:
        item = MenuDirectory(
            name=m.name,
            is_show=m.is_show,
            is_parent=m.is_parent
        )
        item.url = m.url if m.url else None
        item.fa_icon = m.fa_icon if m.fa_icon else None
        # item.parent=int(MenuDirectory.objects.get(pk=m.parent.pk).pk) if m.parent  else None
        item.sorting = m.sorting if m.sorting else None
        item.save()
    return render(request, 'Destek/Desktek-ekle.html', {})
