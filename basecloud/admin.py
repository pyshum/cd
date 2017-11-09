from django.contrib import admin

# Register your models here.

from .forms import CreateOrderForm, CustomersProfileForm, SignUpForm
from .models import SignUp, Status, CustomersOrder, CustomersProfile

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["full_name"]
	form = SignUpForm

class CustomersOrderAdmin(admin.ModelAdmin):
	list_display = ["image"]
	form = CreateOrderForm

class CustomersProfileAdmin(admin.ModelAdmin):
	list_display = ["user"]
	form = CustomersProfileForm

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Status)
admin.site.register(CustomersOrder)
admin.site.register(CustomersProfile)