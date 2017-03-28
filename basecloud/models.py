# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class SignUp(models.Model):
	email = models.EmailField(unique=True)
	full_name = models.CharField(max_length=120, blank=True, null=True, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	# updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	image = models.ImageField(
			null=True, 
			blank=True,
			width_field="width_field",
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
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

class CustomersProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return unicode(self.user)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		CustomersProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	CustomersProfile.user.save()