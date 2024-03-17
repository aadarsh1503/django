from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.conf import settings
from faker import Faker
from django.contrib.auth.models import User

class Receipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    receipe_name = models.CharField(max_length=255)
    receipe_descriptions = models.TextField()
    receipe_price=models.IntegerField(default=0)
    receipe_image = models.ImageField(upload_to ='receipe_images/')
    receipe_view_count=models.IntegerField(default=1)
    ratings = models.PositiveIntegerField(default=0)

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self):
          return f"{self.subject_name}"
      

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return  f"{self.department}"

    class Meta:
        ordering = ['department']



class Studentid(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_id}"

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(Studentid, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=10)
    student_address = models.CharField(max_length=100)

    def __str__(self):
          return f"{self.student_name}"
    class Meta:
        ordering = ['student_name']


class SubjectMarks(models.Model):
    student=models.ForeignKey(Student,related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()
    

    def __str__(self):
          return f"{self.student.student_name}{self.subject.subject_name}"
    class Meta:
        unique_together=['student','subject']


class ReportRank(models.Model):
    student=models.ForeignKey(Student,related_name="studentreportcard",on_delete=models.CASCADE)
    student_rank=models.IntegerField()
    date_of_report_card_generation=models.DateField(auto_created=True)

class Meta:
        unique_together=['student_rank','date_of_report_card_generation']


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipe = models.ForeignKey(Receipe, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()




class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    receipe_name = models.CharField(max_length=255)
    receipe_descriptions = models.TextField()
    receipe_image = models.ImageField(upload_to ='receipe_images/')
    receipe_price=models.IntegerField(default=0)
    receipe_view_count=models.IntegerField(default=1)

class Burger(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    receipe_name = models.CharField(max_length=255)
    receipe_descriptions = models.TextField()
    receipe_image = models.ImageField(upload_to ='receipe_images/')
    receipe_price=models.IntegerField(default=0)
    receipe_view_count=models.IntegerField(default=1)   

class Pizza(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    receipe_name = models.CharField(max_length=255)
    receipe_descriptions = models.TextField()
    receipe_image = models.ImageField(upload_to ='receipe_images/')
    receipe_view_count=models.IntegerField(default=1)       


class User_burger(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    receipe_name = models.CharField(max_length=255)
    receipe_descriptions = models.TextField()
    receipe_image = models.ImageField(upload_to ='receipe_images/')
    receipe_view_count=models.IntegerField(default=1)

class User_pizza(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    receipe_name = models.CharField(max_length=255)
    receipe_descriptions = models.TextField()
    receipe_image = models.ImageField(upload_to ='receipe_images/')
    receipe_view_count=models.IntegerField(default=1)

class Payment(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    cardname = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=16)
    expmonth = models.CharField(max_length=20)
    expyear = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)
    sameadr = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
 
    def __str__(self):
        return self.name

class Addcart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    receipe_name = models.CharField(max_length=255)
    receipe_descriptions = models.TextField()
    receipe_price=models.IntegerField(default=0)
    receipe_image = models.ImageField(upload_to ='receipe_images/')
    receipe_view_count=models.IntegerField(default=1)
    
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
