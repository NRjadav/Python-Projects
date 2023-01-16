from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'myapp/index.html')

@csrf_exempt
def add_student(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        print("========> NAME",name)
        sid=Student.objects.create(name=name,email=email)
        data=Student.objects.values()
        alldata=list(data)
        contaxt={
            'msg':"Successfully added",
            'udata':alldata,
        }
        return JsonResponse({'contaxt':contaxt})

@csrf_exempt
def update_student(request):
    sid=Student.objects.all()
    contaxt={
        'sid':sid,
    }
    return render(request,'myapp/index.html',contaxt)
    
     
