from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#costomized model hear

class Userinfo(models.Model):
    
    userinfo_name=models.CharField(max_length=150)
    userinfo_Uname=models.CharField(max_length=150)
    userinfo_Ftname=models.CharField(max_length=150)
    userinfo_Mtname=models.CharField(max_length=150)
    userinfo_email=models.EmailField(max_length=150)
    userinfo_userpic=models.ImageField(max_length=150,upload_to='user_pic')
    userinfo_phoneno1=models.CharField(max_length=150)
    userinfo_phoneno2=models.CharField(max_length=150)
    userinfo_phoneno3=models.CharField(max_length=150)
    userinfo_password=models.CharField(max_length=150)
    userinfo_gender=models.CharField(max_length=150)
    userinfo_Edulvl=models.CharField(max_length=150)
    userinfo_Expedu=models.CharField(max_length=150)
    userinfo_State=models.CharField(max_length=150)
    userinfo_City=models.CharField(max_length=150)
    userinfo_Zip=models.CharField(max_length=150)
    userinfo_DoB=models.DateField(auto_now=False, auto_now_add=False,)
    userinfo_jdate = models.DateTimeField(auto_now_add=True)
    DisplayFields=['userinfo_name','userinfo_Uname','userinfo_Ftname','userinfo_Mtname','userinfo_email','userinfo_userpic',
                   'userinfo_phoneno1','userinfo_phoneno2','userinfo_phoneno3','userinfo_password','userinfo_gender','userinfo_Edulvl',
                   'userinfo_Expedu','userinfo_State','userinfo_City','userinfo_Zip','userinfo_DoB','userinfo_jdate','userinfo_jdate']
    SearchablFields=['userinfo_name','userinfo_Uname']
    def __str__(self):
        return self.userinfo_Uname