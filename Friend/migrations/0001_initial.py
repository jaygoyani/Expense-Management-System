# Generated by Django 2.1.5 on 2019-03-16 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='friendexpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adder_user', models.CharField(max_length=50)),
                ('payyer_user', models.CharField(max_length=50)),
                ('receiver_user', models.CharField(max_length=50)),
                ('tran_id', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=50)),
                ('details2', models.CharField(max_length=50)),
                ('amount', models.FloatField(blank=True, default=0)),
                ('exp_fri_date', models.DateField(auto_now_add=True)),
                ('exp_fri_datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('exptype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='friends1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=50)),
                ('user2', models.CharField(max_length=50)),
                ('friend_id', models.CharField(max_length=50)),
                ('amount1', models.FloatField(blank=True, default=0)),
            ],
        ),
    ]
