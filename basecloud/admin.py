from django.contrib import admin

# Register your models here.

from .forms import *
from .models import *

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["full_name"]
	form = SignUpForm

class CustomersOrderAdmin(admin.ModelAdmin):
	list_display = ["title"]
	form = CreateOrderForm

class CustomersProfileAdmin(admin.ModelAdmin):
	list_display = ["user"]
	form = CustomersProfileForm

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Status)
admin.site.register(CustomersOrder)
admin.site.register(CustomersProfile)