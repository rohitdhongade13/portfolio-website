from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        dese = request.POST['dese']
        c = Contact(name=name,phone=phone, email=email, dese=dese)
        c.save()
    return render(request,"contact.html")