# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	# updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	# stl_file = models.FileField(blank=True, null=True)

	def __unicode__(self):
		return self.email

class Status(models.Model):
	name = models.CharField(max_length=30, verbose_name='Статус')
	class Meta:
		verbose_name = 'статусы'
		verbose_name_plural = 'Статус'
	def __unicode__(self):
		return self.name

class CustomersOrder(models.Model):
	title = models.CharField(max_length=100, verbose_name='Название')
	create_date = models.TextField(verbose_name='Описание')
	user = models.ForeignKey(User)
	rate = models.IntegerField(verbose_name='Рейтинг', default=0)
	image = models.ImageField(
			null=True, 
			blank=True,
			width_field="width_field",
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)