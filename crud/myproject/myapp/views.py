from django.shortcuts import render,redirect
from .models import*
# Create your views here.


def crud(request):
    uid=user.objects.all()
    contaxt={
        'uid':uid
    }
    return render(request,"myapp/crud.html",contaxt)

def create_data(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']

        user.objects.create(name=name,
                            email=email,
                            address=address,
                            phone=phone) 
        
        

    return redirect("crud")


def update_data(request,id):
    uid=user.objects.get(id=id)
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']

        uid.name=name
        uid.name=name
        uid.address=address
        uid.phone=phone 
        uid.save()

    return redirect("crud")

    # return render(request,"myapp/crud.html",contaxt)

def delete_data(request,id):
    uid=user.objects.get(id=id)
    uid.delete()
    return redirect("crud")
