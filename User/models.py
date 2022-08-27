from django.db import models
from django.utils.timezone import now


# Create your models here.
class user_exp(models.Model):
    username = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    exp_type = models.CharField(max_length=50)
    exp_details = models.CharField(max_length=250)
    exp_date = models.DateField(auto_now_add=True)
    exp_datetime = models.DateTimeField(default=now, editable=False)
    exp_amount = models.FloatField()

class user_exp1(models.Model):
    username = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
