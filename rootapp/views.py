from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from gmailpr import settings
from .models import UserNotification

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        UserNotification.objects.create(name=name,email=email,message=message)

        send_mail(
            subject = f"Yangi habar {name} dan",
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [email],
            fail_silently = False,
        )
        return HttpResponseRedirect('/success/')
    return render(request, 'index.html')