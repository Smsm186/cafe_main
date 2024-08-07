from django.shortcuts import render, redirect
from .models import Mail

# Create your views here.


def main(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
            mail = Mail()
            mail.name = request.POST.get('name')
            mail.mail = request.POST.get('email')
            mail.message = request.POST.get('message')
            mail.save()
            return render(request, "index.html")
        else:
            return render(request, "index.html")
    return render(request, "index.html")