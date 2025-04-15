from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('message')
        date=datetime.today()
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=date)
        contact.save()
        messages.success(request, "Your Message Has Been Sent.")
    return render(request,'contact.html')

def services(request):
    return render(request,'service.html')