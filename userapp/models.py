from django.db import models
from adminapp.models import*
# Create your models here.
class Reg(models.Model):
    Uname=models.CharField(max_length=23)
    Age=models.IntegerField()
    Phn=models.IntegerField()
    Email=models.EmailField()
    Address=models.CharField(max_length=130)
    Pincode=models.IntegerField()
    Password=models.CharField(max_length=23)
    Repass=models.CharField(max_length=23)


class CONT(models.Model):
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20)
    Email=models.EmailField()
    Subject=models.CharField(max_length=200)
    Message=models.CharField(max_length=250)

class BOOK(models.Model):
    userreg=models.ForeignKey(Reg,on_delete=models.CASCADE,null=True)
    ServiceID=models.ForeignKey(SERVICES,on_delete=models.CASCADE,null=True)
    saloID=models.ForeignKey(SALOON,on_delete=models.CASCADE,null=True)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20,default='9AM-1PM')
    Note=models.CharField(max_length=250)
    status=models.CharField(max_length=10,default='disapprove')
   