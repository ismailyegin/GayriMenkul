from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render


def help(request):


    if request.method == 'POST':
        user = request.user
        konu=request.POST['konu']
        icerik= request.POST['icerik']
        if konu and icerik:
            try:
                konu = "["+user.email +  "] - "+konu
                send_mail(konu, icerik, 'info@kobiltek.com', ['info@kobiltek.com'])
                messages.success(request, 'Yardım ve Destek talebi basari ile gönderilmistir.')
            except BadHeaderError:
                print('Invalid header found.')
                messages.warning(request, 'Alanları Kontrol Ediniz Bir Şeyler Ters Gitti')
    return render(request,'yardım/help.html')