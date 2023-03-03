from django.db import models

# Create your models here.

class User(models.Model):
    email=models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=10)
    role=models.CharField(max_length=10)

    def __str__(self):
        return self.email
    

class Owner(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    contect_no=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=30)
    email=models.EmailField(unique=True,max_length=30)
    house_no=models.CharField(max_length=20)
    family_member=models.CharField(max_length=20)
    no_of_vihical=models.CharField(max_length=20)
    pic=models.FileField(upload_to='media/images/',default='media/images/set.png.png')

class Notice(models.Model):
    notice_name=models.CharField(max_length=30)
    notice_topic=models.TextField()
    notice_date=models.DateTimeField()

class Sell_Home(models.Model):
    owner_name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=30)
    email=models.EmailField(unique=True,max_length=30)
    house_no=models.CharField(max_length=20)
    family_member=models.CharField(max_length=20)
    pic=models.FileField(upload_to='media/images/',default='media/images/s1.jpg')



    