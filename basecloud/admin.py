from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import *

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["full_name"]
	form = SignUpForm


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Status)
admin.site.register(CustomersOrder)