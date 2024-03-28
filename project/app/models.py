from django.db import models

class Member(models.Model):
    idno=models.IntegerField()
    firstname = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    by=models.CharField(max_length=2)
    chat=models.CharField(max_length=255)