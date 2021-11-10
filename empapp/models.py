from django.db import models

# Create your models here.


class manager(models.Model):
    rmp=models.CharField(max_length=20)


class Employee(models.Model):
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    employeid=models.IntegerField()
    phonenumber=models.IntegerField()
    email=models.EmailField()
    rmp=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.IntegerField()





