from django.shortcuts import render
from .models import*

# Create your views here.

def index(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='Owner':
            oid=Owner.objects.get(user_id=uid)
            request.session['email']=uid.email
            print("============>",oid.name)
            contaxt={
                'uid':uid,
                'oid':oid,
            }
            return render(request,'myapp/index.html',contaxt)
    else:
        return render(request,'myapp/login.html')        

def login(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='Owner':
            oid=Owner.objects.get(user_id=uid)
            request.session['email']=uid.email
            print("============>",oid.name)
            contaxt={
                'uid':uid,
                'oid':oid,
            }
            return render(request,'myapp/index.html',contaxt)
    else:    
        if request.POST:
            email=request.POST['emailname']
            password=request.POST['passwordname']
            print("=================>",email)
            uid=User.objects.get(email=email)
            if uid.password==password:
                if uid.role=='Owner':
                    oid=Owner.objects.get(user_id=uid)
                    request.session['email']=uid.email
                    print("================>",oid.name)
                    contaxt={
                        'uid':uid,
                        'oid':oid,
                    }
                    return render(request,'myapp/index.html',contaxt)
                # else:
                #     return render(request,'myapp/login.html')        
            else:
                contaxt={
                    'e_msg':'invlaid password'
                }  
                return render(request,'myapp/login.html',contaxt) 
        else:
            return render(request,'myapp/login.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,'myapp/login.html')
    else:
        return render(request,'myapp/login.html')    

def profile(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Owner":
            oid=Owner.objects.get(user_id=uid)
            request.session['email']=uid.email
            contaxt={
                'uid':uid,
                'oid':oid,
            } 
            return render(request,'myapp/profile.html',contaxt)
    else:
        return render(request,'myapp/login.html')

def change_password(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Owner":
            oid=Owner.objects.get(user_id=uid)
            request.session['email']=uid.email
            current_password=request.POST['current_password']
            new_password=request.POST ['new_password']
            if request.POST:
                if uid.password==current_password:
                    uid.password=new_password
                    uid.save()
                    return render(request,'myapp/profile.html')
                else:
                    return render(request,'myapp/profile.html')        
    else:
        return render(request,'myapp/login.html')

def update_profile(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Owner":
            oid=Owner.objects.get(user_id=uid)
            request.session['email']=uid.email
            name=request.POST['name']
            contact_no=request.POST['contact_no']
            if request.POST:
                oid.name=name
                oid.contect_no=contact_no
                oid.save()
                return render(request,'myapp/profile.html')    
    else: 
        return render(request,'myapp/login.html') 

def add_member(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Owner":
            oid=Owner.objects.get(user_id=uid)
            if request.POST:
                name=request.POST['name']
                age=request.POST['age']
                gender=request.POST['gender']
                contact_no=request.POST['contact_no']
                email=request.POST['email']
                house_no=request.POST['house_no']
                family_member=request.POST['family_member']
                no_of_vihical=request.POST['no_of_vihical']
                # pic=request.POST['pic']

                mid=Member.objects.create(user_id=uid,
                                          name=name,
                                          age=age,
                                          gender=gender,
                                          contact_no=contact_no,
                                          email=email,
                                          house_no=house_no,
                                          family_member=family_member,
                                          no_of_vihical=no_of_vihical,
                                        #   pic=pic
                                          )
            contaxt={
                'uid':uid,
                'oid':oid,
                # 'mid':mid,
            }                          
            return render(request,'myapp/add_member.html',contaxt) 
    else:
        contaxt={
                    'uid':uid,
                    'oid':oid
                    # 'mid':mid,
                } 
        return render(request,'myapp/login.html',contaxt)

def all_members(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='Owner':
            oid=Owner.objects.get(user_id=uid)
            mall=Member.objects.all()
            contaxt={
                'uid':uid,
                'oid':oid,
                'mall':mall,
            }
        return render(request,'myapp/all_members.html',contaxt)        

def image(request):
    return render(request,'myapp/image.html')

def add_notice(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='Owner':
            oid=Owner.objects.get(user_id=uid)
            if request.POST:
                notice_name=request.POST['notice_name']
                notice_topic=request.POST['notice_topic']
                notice_date=request.POST['notice_date']

                nid=Notice.objects.create(notice_name=notice_name,
                                          notice_topic=notice_topic,
                                          notice_date=notice_date)
            
            contaxt={
                'uid':uid,
                'oid':oid,
                # 'nid':nid

            }
            return render(request,'myapp/add_notice.html',contaxt)
    else:
        contaxt={
                'uid':uid,
                'oid':oid,
                'nid':nid

            }
        return render(request,'myapp/add_notice.html',contaxt)        

def sell_home(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="Owner":
            oid=Owner.objects.get(user_id=uid)
            if request.POST:
                owner_name=request.POST['owner_name']
                price=request.POST['price']
                address=request.POST['address']
                contact_no=request.POST['contact_no']
                email=request.POST['email']
                house_no=request.POST['house_no']
                family_member=request.POST['family_member']
                # no_of_vihical=request.POST['no_of_vihical']
                # pic=request.POST['pic']

                sid=Sell_Home.objects.create(owner_name=owner_name,
                                          price=price,
                                          address=address,
                                          contact_no=contact_no,
                                          email=email,
                                          house_no=house_no,
                                          family_member=family_member,
                                        #   no_of_vihical=no_of_vihical,
                                        #   pic=pic
                                          )
            contaxt={
                'uid':uid,
                'oid':oid,
                # 'mid':mid,
            }                          
            return render(request,'myapp/sell_home.html',contaxt) 

    else:
        contaxt={
                'uid':uid,
                'oid':oid,
                'sid':sid,

            }
        return render(request,'myapp/sell_home.html',contaxt)   

def buy_home(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='Owner':
            oid=Owner.objects.get(user_id=uid)
            mall=Member.objects.all()
            sall=Sell_Home.objects.all()
            contaxt={
                'uid':uid,
                'oid':oid,
                'mall':mall,
                'sall':sall,
            }
       
        return render(request,'myapp/buy_home.html',contaxt)

