from datetime import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from sbs.Forms.UserSearchForm import UserSearchForm
from sbs.models.Logs import Logs
from sbs.services import general_methods


# page
# from sbs.models.simplecategory import simlecategory

@login_required
def return_log(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    logs = Logs.objects.none()
    user_form = UserSearchForm()
    if request.method == 'POST':
        user_form = UserSearchForm(request.POST)
        if user_form.is_valid():
            firstName = user_form.cleaned_data.get('first_name')
            lastName = user_form.cleaned_data.get('last_name')
            email = user_form.cleaned_data.get('email')
            playDate = request.POST.get('start')
            finishDate = request.POST.get('End')
            if playDate:
                playDate = datetime.strptime(playDate, '%d/%m/%Y').date()

            if finishDate:
                finishDate = datetime.strptime(finishDate, "%d/%m/%Y").date()

            if not (firstName or lastName or email or playDate or finishDate):
                logs = Logs.objects.filter(kobilid=2).order_by('-creationDate')

            else:
                query = Q()
                if lastName:
                    query &= Q(user__last_name__icontains=lastName)
                if firstName:
                    query &= Q(user__first_name__icontains=firstName)
                if email:
                    query &= Q(user__email__icontains=email)
                if playDate:
                    query &= Q(creationDate__gte=playDate)
                if finishDate:
                    query &= Q(creationDate__lt=finishDate)

                logs = Logs.objects.filter(kobilid=2).filter(query).order_by('-creationDate')
    return render(request, 'Log/Logs.html', {'logs': logs, 'user_form': user_form})
