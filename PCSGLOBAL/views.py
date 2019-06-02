from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from PCSGLOBAL.models import Mysite

from .models import Mysite


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fname')
        lnm = request.POST.get('lname')
        em = request.POST.get('email')
        do = request.POST.get('dob')
        mo = request.POST.get('phone')
        gn = request.POST.get('gender')
        pa = request.POST.get('password')
        data = fnm + '\n' + lnm + '\n' + em + '\n' + do + '\n' + mo + '\n' + gn + '\n' + pa
        value = Mysite(fname=fnm, lname=lnm, email=em, dob=do, phone=mo, gender=gn, password=pa)
        value.save()
        # send data in mail
        subject = 'user information'
        message = 'Thank you for giving details' + '\n' + data
        from_email = settings.EMAIL_HOST_USER
        to_email = [value.email]
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        return render(request, "index.html")

    else:
        return render(request, "index.html")


def about(request):
    return render(request, 'About.html')


def data_science(request):
    return render(request, 'Data_science.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def industry(request):
    return render(request, 'Industry.html')


def products(request):
    return render(request, 'Product.html')


def careers(request):
    return render(request, 'Careers.html')


def services(request):
    return render(request, 'Services.html')


def contact(request):
    return render(request, 'Contact_us.html')


def login(request):
    return render(request, 'login.html')

def signup_page(request):
    return  render(request, 'signup.html')


def user_home(request):
    return render(request, 'user_home.html')

def admin(request):
    return render(request, 'admin.html')


