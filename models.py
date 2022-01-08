import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FinancePeer.settings")


from django.db import models
from django.contrib.auth.models import User

class loginTab(models.Model):
    username = models.CharField(max_length=200, default="  ")
    email_id = models.EmailField(max_length=150,unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "loginTab"

import django
from django.utils import timezone

class FinancePeerJsonTab(models.Model):
    email_id = models.EmailField(max_length=150)
    JsonFile = models.FileField()                    #upload_to=''
    class Meta:
        db_table = "FinancePeerJsonTab"

class FinancePeerDetailsTab(models.Model):
   FP_ID  = models.IntegerField(unique=True)
   FP_UserID = models.IntegerField()
   FP_Title = models.CharField(unique=True,max_length=150)
   FP_Body = models.TextField(max_length=500)

   class Meta:
      db_table = "FinancePeerDetailsTab"

