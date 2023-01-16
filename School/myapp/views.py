from django.shortcuts import render
from . models import*

# Create your views here.


def index(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=='Hod':
            hid=Hod.objects.get(user_id=sid)
            contaxt={
                'sid':sid,
                'hid':hid,
            }
            return render(request,'myapp/index.html',contaxt)
    
    else:
        return render(request,'myapp/login.html') 

   
def login(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=='Hod':
            hid=Hod.objects.get(user_id=sid)
            contaxt={
                'sid':sid,
                'hid':hid,
            }
            return render(request,'myapp/index.html',contaxt)
    else:    

        if request.POST:
            email=request.POST['emailname']
            password=request.POST['passwordname']
            print("============>",email)

            sid=Student.objects.get(email=email)
            if sid.password==password:
                if sid.role=="Hod":
                    hid=Hod.objects.get(user_id=sid)
                    request.session['email']=sid.email
                    contaxt={
                        'sid':sid,
                        'hid':hid,
                    }

                    return render(request,'myapp/index.html',contaxt)
            else:
                contaxt={
                    's_msg': 'wrong password' 
                } 
                return render(request,'myapp/login.html',contaxt)        

        else:
            return render(request,'myapp/login.html') 

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,'myapp/login.html')

def profile(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=="Hod":
            hid=Hod.objects.get(user_id=sid)
            nsid=New_Student.objects.values()
            contaxt={
                'sid':sid,
                'hid':hid,
                'nsid':nsid,
            }
    return render(request,'myapp/profile.html',contaxt) 

def change_password(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=='Hod':
            hid=Hod.objects.get(user_id=sid)
            if request.POST:
                currentpassword=request.POST['currentpassword']
                newpassword=request.POST['newpassword']
                if sid.password==currentpassword:
                    sid.password=newpassword
                    sid.save()
                
            return render(request,'myapp/profile.html')

def update_profile(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=='Hod':
            hid=Hod.objects.get(user_id=sid)
            if request.POST:
                username=request.POST['username']
                hid.username=username
                hid.save()
            return render(request,'myapp/profile.html')

def add_student(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=='Hod':
            hid=Hod.objects.get(user_id=sid)
            if request.POST:
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']
                fathername=request.POST['fathername']   
                mothername=request.POST['mothername']
                dob=request.POST['dob']
                std=request.POST['std']
                gender=request.POST['gender']
                phone=request.POST['phone']
                email=request.POST['email']

                nsid=New_Student.objects.create(firstname=firstname,
                                                lastname=lastname,
                                                fathername=fathername,
                                                mothername=mothername,
                                                dob=dob,
                                                std=std,
                                                gender=gender,
                                                phone=phone,
                                                email=email,)

                contaxt={
                    'sid':sid,
                    'hid':hid,
                    'nsid':nsid,
                }                                
                return render(request,'myapp/add_student.html',contaxt)
            
            else:
                contaxt={
                    'sid':sid,
                    'hid':hid,
                    # 'nsid':nsid,
                }                                
                return render(request,'myapp/add_student.html',contaxt)

def all_students(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=='Hod':
            hid=Hod.objects.get(user_id=sid)
            nsall=New_Student.objects.all()
            contaxt={
                'sid':sid,
                'hid':hid,
                'nsall':nsall,
            }
        return render(request,'myapp/all_students.html',contaxt)                

 
def add_teacher(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=="Hod":
            hid=Hod.objects.get(user_id=sid)
            if request.POST:
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']
                dob=request.POST['dob']
                gender=request.POST['gender']
                special_subject=request.POST['special_subject']
                phone=request.POST['phone']
                email=request.POST['email']
                experience=request.POST['experience']

                tall=Teacher.objects.create(firstname=firstname,
                                            lastname=lastname,
                                            dob=dob,
                                            gender=gender,
                                            special_subject=special_subject,
                                            phone=phone,
                                            email=email,
                                            experience=experience)    
    return render(request,'myapp/add_teacher.html')

def all_teachers(request):
    if 'email' in request.session:
        sid=Student.objects.get(email=request.session['email'])
        if sid.role=="Hod":
            hid=Hod.objects.get(user_id=sid)
            tall=Teacher.objects.all()
            contaxt={
                'sid':sid,
                'hid':hid,
                'tall':tall,
            }
        return render(request,'myapp/all_teachers.html',contaxt)

def time_table(request):
    return render(request,'myapp/time_table.html')

def evants_photo(request):
    return render(request,'myapp/evants_photo.html')    