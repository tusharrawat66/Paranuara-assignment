from django.db import models
from datetime import datetime
from django_mysql.models import JSONField

from django.core.validators import MinLengthValidator,MaxLengthValidator




class Company(models.Model):
    index = models.IntegerField(db_column='index', default=0, null=False)
    company = models.CharField(db_column='company', max_length=255, null=False)

    class Meta:
        managed = True
        db_table = 'company'


class People(models.Model):
    uid = models.CharField(db_column='uid', max_length=128, primary_key=True, unique=True, blank=False)
    index = models.IntegerField(db_column='index', null=False)
    guid = models.CharField(db_column='guid', max_length=100, null=True)
    has_died = models.BooleanField(db_column='has_died', null=False, default=False)
    balance = models.CharField(db_column='balance', max_length=20, null=True)
    picture = models.CharField(db_column='picture', null=True, max_length=200)
    age = models.IntegerField(db_column='age', null=True)
    eye_color = models.CharField(db_column='eye_color', null=True, max_length=20)
    name = models.CharField(db_column='name', null=False, max_length=100)
    gender = models.CharField(db_column='gender', null=True, max_length=20)
    company_id = models.IntegerField(db_column='company_id', null=False, default=0)

    email = models.CharField(db_column='email', unique=True, null=True, max_length=200)
    phone = models.CharField(validators=[MinLengthValidator(17), MaxLengthValidator(20)], db_column='phone', null=True, max_length=20)
    address = models.CharField(db_column='address', null=True, max_length=255)
    about = models.CharField(db_column='about', null=True, max_length=1000)
    registered = models.DateTimeField(db_column='registered', null=False, default=datetime.utcnow)
    tags = JSONField(db_column='tags', default=list)
    friends = JSONField(db_column='friends', default=list)
    greeting = models.CharField(db_column='greeting', null=True, max_length=200)
    favouriteFood = JSONField(db_column='favouriteFood')
    favourite_fruit = JSONField(db_column='favourite_fruit', default=list)
    favourite_vegetable = JSONField(db_column='favourite_vegetable', default=list)

    class Meta:
        managed = True
        db_table = 'people'


class Txnhist(models.Model):
    date = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    user = models.CharField(db_column='user', null=True, max_length=20)
    method = models.CharField(db_column='method', null=True, max_length=20)
    api = models.CharField(db_column='api', null=True, max_length=100)
    parameter = JSONField(db_column='parameter', default=list)

    class Meta:
        managed = True
        db_table = 'txnhist'

