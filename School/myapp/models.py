from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True , max_length=30)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=10)

class Hod(models.Model):
    user_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    pic=models.FileField(upload_to='media/images/',default='media/images/pic.jpg') 

class New_Student(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    fathername=models.CharField(max_length=30)
    mothername=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    std=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    pic=models.FileField(upload_to='media/images',default='media/images/pic.jpg')     

class Teacher(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    special_subject=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    experience=models.CharField(max_length=30)
    pic=models.FileField(upload_to='media/images',default='media/images/teacher1.jpg') 



