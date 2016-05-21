from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	

	return render(request, "home.html")

def clients_profile(request):
	if request.user.is_authenticated():
		title = 'You are logged in as %s' %(request.user)
		photo = '/static/img/All_OSs.jpg'
		context = {
			"title": title,
			"photo": photo,
		}


	return render(request, "profile_client.html", context)