from django.db import models

# Create your models here.

class group_c(models.Model):
    gname = models.CharField(max_length=50)
    f1 = models.CharField(max_length=50)
    f2 = models.CharField(max_length=50)
    f3 = models.CharField(max_length=50)
    f4 = models.CharField(max_length=50)
    f5 = models.CharField(max_length=50)
    f6 = models.CharField(max_length=50)
    f7 = models.CharField(max_length=50)
    f8 = models.CharField(max_length=50)
    f9 = models.CharField(max_length=50)
    f10 = models.CharField(max_length=50)
    creater = models.CharField(max_length=50)

class groupe(models.Model):
    ename = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    amount1 = models.CharField(max_length=50)


class groupmember(models.Model):
    user = models.CharField(max_length=50)
    groupdetails = models.CharField(max_length=1000)

