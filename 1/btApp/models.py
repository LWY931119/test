from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
class Data(models.Model):
	name = models.CharField(max_length=30)
	data = models.FloatField()
	time = models.DateTimeField(auto_now_add=True)
class Datas(models.Model):
	name = models.CharField(max_length=30)
	data = models.FloatField()
	time = models.DateTimeField(auto_now_add=True)
class Tem(models.Model):
	data = models.FloatField()
	time = models.DateTimeField(auto_now_add =True)
class Moi(models.Model):
	data = models.FloatField()
	time = models.DateTimeField(auto_now_add = True)
class Co2(models.Model):
	data = models.FloatField()
	time = models.DateTimeField(auto_now_add = True)
class Lig(models.Model):
	data = models.FloatField()
	time = models.DateTimeField(auto_now_add = True)