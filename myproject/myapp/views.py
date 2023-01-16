from django.shortcuts import render
from .models import *
import random
import datetime
# Create your views here.

def home(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=="Chairmans":
                    cid=Chairman.objects.get(user_id=uid)
                    print(cid.username)
                    request.session['email']=uid.email
                    contaxt={
                        'uid':uid,
                        'cid':cid
                    } 
                    return render(request,"myapp/index.html",contaxt)
    else:
        return render(request,'myapp/login.html')    

def login(request):
    print("LOGIN PAGE REFRENCE")
    if 'email' in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            print(cid.username)
            request.session['email']=uid.email
            contaxt={
                'uid':uid,
                'cid':cid
            } 
            return render(request,"myapp/index.html",contaxt)
    else:
        if request.POST:
            email=request.POST["emailname"]
            password=request.POST["passwordname"]
            print("======>EMAIL" ,email)
            # print("======>password",password)

            uid=User.objects.get(email=email)
            if uid.password==password:
                if uid.role=="Chairmans":
                    cid=Chairman.objects.get(user_id=uid)
                    print(cid.username)
                    request.session['email']=uid.email
                    contaxt={
                        'uid':uid,
                        'cid':cid
                    }
                    return render(request,"myapp/index.html",contaxt)
                    
            else:
                # print("Invalid password") 
                context={
                    'e_msg':'Invalid password'
                }
                return render(request,"myapp/login.html",context)
        else:
            print("LOGIN PAGE REFRENCE")
            return render(request,"myapp/login.html")

def logout(request):
    if  "email" in request.session:
        del request.session["email"]
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def profile(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            print(cid.username)
            request.session['email']=uid.email
            contaxt={
                'uid':uid,
                'cid':cid
            } 
            return render(request,"myapp/profile.html",contaxt)

def add_member(request):    
    if 'email' in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            
            if request.POST:
                email=request.POST['email']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']
                contact_no=request.POST['contact_no']
                family_member=request.POST['family_member']
                block_number=request.POST['block_number']
                house_number=request.POST['house_number']
                no_of_vehicle=request.POST['no_of_vehicle']
                occupation=request.POST['occupation']
                job_loction=request.POST['job_loction']

                l1=['adffjhsjk','3hhjh5','123544456','DSJSAJI']
                password=random.choice(l1)+email[3:6]+str(contact_no[3:6])
                uid=User.objects.create(email=email,password=password,role="member")
                mid=Member.objects.create(user_id=uid,firstname=firstname,
                                          lastname=lastname,
                                          contact_no=contact_no,
                                          family_member=family_member,
                                          occupation=occupation,
                                          job_loction=job_loction,
                                          block_number=block_number,
                                          house_number=house_number,
                                          no_of_vehicle=no_of_vehicle,
                                          )   
                
                print("=======>",firstname)
                contaxt={
                'uid':uid,
                'cid':cid,
                'mid':mid,
                's_msg':"successfully member created"   
                } 
                return render(request,'myapp/add_member.html',contaxt)    
            
            
            else:
                contaxt={
                    'uid':uid,
                    'cid':cid
                } 
                return render(request,"myapp/add_member.html",contaxt)      
                
def change_password(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            current_password=request.POST['current_password']
            new_password=request.POST['new_password']
            if request.POST:
                if uid.password==current_password:
                    uid.password=new_password
                    uid.save()

                context={
                    'uid':uid,
                    'cid':cid
                }
                return render(request,'myapp/profile.html',context)
            else:
                context={
                    'uid':uid,
                    'cid':cid
                }
                return render(request,'myapp/profile.html',context)

def update_profile_chairman(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='Chairmans':
            cid=Chairman.objects.get(user_id=uid)
            if request.POST:
                username=request.POST['username']
                if "picture" in request.FILES:
                    cid.pic=request.FILES['picture']
                    cid.save()
                cid.username=username
                cid.save()

                context={
                    'uid':uid,
                    'cid':cid,
                }
                return render(request,'myapp/profile.html',context)
            else:
                context={
                    'uid':uid,
                    'cid':cid
                }
                return render(request,'myapp/profile.html',context) 

def add_notice(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            
            if request.POST:
                title=request.POST['title']
                description=request.POST['description']
                # pic=request.FILES['pic'] 
                

                print("======>" ,title)       
                nid=Notice.objects.create(title=title,
                                          description=description,
                                        #   pic=pic,
                                          
                                          
                                          )   
                
                contaxt={
                    'uid':uid,
                    'cid':cid,
                    'nid':nid
                    
                }                          
                return render(request,'myapp/add_notice.html',contaxt)

            else:
                contaxt={
                    'uid':uid,
                    'cid':cid,
                    
                }                          
                return render(request,'myapp/add_notice.html',contaxt)


def view_members(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            mall=Member.objects.all()
            context={
                'uid':uid,
                'cid':cid,
                'mall':mall,
            }
    return render(request,'myapp/view_members.html',context)

def view_notice(request):    
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            nall=Notice.objects.all()
            context={
                'uid':uid,
                'cid':cid,
                'nall':nall
            }

    return render(request,'myapp/view_notice.html',context)

def add_evant(request):

    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            if request.POST:
                name=request.POST['name']
                print("=====>",name)
            #     # video=request.FILES['video']
                eid=Event.objects.create(name=name)
                context={
                    'uid':uid,
                    'cid':cid,
                    'eid':eid
                }
                return render(request,'myapp/add_evant.html',context)
            else:
                context={
                    'uid':uid,
                    'cid':cid,
                    
                }
                return render(request,'myapp/add_evant.html',context)

def view_evants(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Chairmans":
            cid=Chairman.objects.get(user_id=uid)
            eall=Event.objects.all()
            contaxt={
                'uid':uid,
                'cid':cid,
                'eall':eall
            }
        return render(request,'myapp/view_evants.html',contaxt)