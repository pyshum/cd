from django import forms
from django.contrib.auth.models import User
from .models import SignUp, CustomersOrder, CustomersProfile, User


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email', 'image']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please make sure you use your USC email.")
		# if not extension == "edu":
		# 	raise forms.ValidationError("Please use a valid .EDU email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#write validation code.
		return full_name

	def clean_image(self):
		image = self.cleaned_data.get('image')
		return image

class CreateOrderForm(forms.ModelForm):
	class Meta:
		model = CustomersOrder
		fields = ('title', 'rate', 'image')


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class CustomersProfileForm(forms.ModelForm):
	class Meta:
		model = CustomersProfile
		fields = ('user', 'website', 'picture')
		