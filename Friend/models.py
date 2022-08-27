from django.db import models
from django.utils.timezone import now

# Create your models here.
class friendexpense(models.Model):
    adder_user = models.CharField(max_length=50)
    payyer_user = models.CharField(max_length=50)
    receiver_user = models.CharField(max_length=50)
    tran_id = models.CharField(max_length=20)
    details = models.CharField(max_length=50)
    details2 = models.CharField(max_length=50)
    amount = models.FloatField(default=0, blank=True)
    exp_fri_date = models.DateField(auto_now_add=True,editable=False)
    exp_fri_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    exptype = models.CharField(max_length=50)

class friends1(models.Model):
    user1 = models.CharField(max_length=50)
    user2 = models.CharField(max_length=50)
    friend_id = models.CharField(max_length=50)
    amount1 = models.FloatField(default=0, blank=True)
