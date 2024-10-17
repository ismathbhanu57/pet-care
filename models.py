from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

class Customer(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    address= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Pending')
    image=models.FileField()

class Notifications(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    ndate_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Notifications"


class Doctors(models.Model):
    name= models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    license_number= models.CharField(max_length=100)
    contact_number= models.BigIntegerField()
    email= models.EmailField()
    password=models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    experience = models.IntegerField()
    image=models.FileField()
    status = models.CharField(max_length=100, default='Pending')


class Pet(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    type=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    weight=models.IntegerField()
    height=models.FloatField()
    color=models.CharField(max_length=100)
    owner=models.CharField(max_length=100)
    image=models.ImageField()
    description=models.CharField(max_length=100)
    sell_for = models.CharField(max_length=100,default='No')
# models.py


class Appoitments(models.Model):
    doctor_email = models.EmailField()
    customer_email = models.EmailField()
    select_pet = models.CharField(max_length=100)
    reason=models.CharField(max_length=100)
    bookings_date_time=models.DateTimeField(auto_now=True)
    appoitments_date_time=models.DateTimeField()
    status = models.CharField(max_length=100, default='Pending')


class Precautions(models.Model):
    email = models.EmailField()
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    pet=models.CharField(max_length=100)
    date_time=models.DateTimeField(auto_now=True)

class Quote(models.Model):
    doctor_email = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=30)
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=20)
    date_time=models.DateTimeField(auto_now=True)

class Prescriptions(models.Model):
    appoitments = models.ForeignKey(Appoitments,on_delete=models.CASCADE)
    doctor_email = models.EmailField()
    customer_email = models.EmailField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    prescription_file = models.FileField()
    date_time=models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    customer_email = models.CharField(max_length=100)
    doctors = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    reviews=models.TextField(max_length=100)
    ratings=models.IntegerField()
    date_time=models.DateTimeField(auto_now=True)

class Admin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Admin"


class Friends_Requests(models.Model):
    customers = models.ForeignKey(Customer,on_delete=models.CASCADE)
    from_email = models.EmailField()
    to_email = models.EmailField()
    status = models.CharField(max_length=100, default='Pending')

    class Meta:
        db_table = "Friends_Requests"
        unique_together = ('from_email', 'to_email')


class Add_Posts(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    only_for = models.CharField(max_length=100)
    pfile = models.FileField()
    status = models.CharField(max_length=100, default='Pending')
    date_time=models.DateTimeField(auto_now=True)

class Likes(models.Model):
    post = models.ForeignKey(Add_Posts, on_delete=models.CASCADE)
    customer_email = models.EmailField()
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('post', 'customer_email')

class Add_Comments(models.Model):
    posts = models.ForeignKey(Add_Posts, on_delete=models.CASCADE)
    customer_email = models.EmailField()

    comments = models.CharField(max_length=100)
    date_time=models.DateTimeField(auto_now=True)

class Interest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    interest_date = models.DateTimeField(auto_now_add=True)

class Pets_Likes(models.Model):
    pets = models.ForeignKey(Pet, on_delete=models.CASCADE)
    customer_email = models.EmailField()
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('pets', 'customer_email')

