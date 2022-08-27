from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=16)
    phone_number = models.BigIntegerField()
    user_id = models.CharField(max_length=50)
