from django.db import models

class Member(models.Model):
    idno=models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    by=models.CharField(max_length=4)
    chat=models.CharField(max_length=255)