from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import *
from .models import *

# Create your views here.
def home(request):
	

	return render(request, "home.html")

def clients_profile(request):
	if request.user.is_authenticated():
		instance = get_object_or_404(CustomersProfile.objects, user_id=request.user.id) #'You are logged in as %s' %(request.user)
        # pro_photo = CustomersProfile.
		# instance = SignUp.objects
        # photo =  user.picture
        context = {
        	"photo": instance.picture,
            "profile_id": request.user.id,
        	# "photo": pro_photo,
        }


	return render(request, "profile_client.html", context)

def create_order(request):
	#if request.user.is_authenticated():
	form = CreateOrderForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		print form.cleaned_data.get("title")
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect('/profile/')
	context = {
	"form": form,
	}

	return render(request, "customers_order.html", context)


def orders_detail(request, customersorder_id=1):
    instance = get_object_or_404(CustomersOrder, pk=customersorder_id)
    #customersorder_id = instance.id
    # if instance.publish > timezone.now().date():
    #     if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    # share_string = quote_plus(instance.content)
    # title = CustomersOrder.title()
    context = {
        "title": instance.title,
        "instance": instance,
        "author": instance.user,
        "customersorder_id": instance.id
        #"order_number": instance.id,
        # "instance": instance,
        # "share_string": share_string,
    }
    return render(request, "orders_detail.html", context)

def orders_list(request):
    # today = timezone.now().date()
    queryset_list = CustomersOrder.objects.all() #.order_by("-timestamp")
    if request.user.is_authenticated:
        queryset_list = CustomersOrder.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(queryset_list, 10) #  Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
         "object_list": queryset,
         "title": "List",
         "page_request_var": page_request_var,
         # "today": today,
        }
    return render(request, "orders_list.html", context)

def order_edit(request, customersorder_id=None):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    instance = get_object_or_404(CustomersOrder, pk=customersorder_id)
    form = CreateOrderForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        print form.cleaned_data.get("title")
        instance.save()
        # message success
        messages.success(request, "Item Saved")
        return HttpResponseRedirect('/orders/')
        # return HttpResponseRedirect('orders_detail/')


    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "customers_order.html", context)

def register(request):
    
    # registered = False

    # if request.method == 'POST':
    # user_form = UserForm(data=request.POST)
    profile_form = CustomersProfileForm(data=request.POST)

    # if user_form.is_valid() and profile_form.is_valid():

    # user = user_form.save()

    # user.set_password(user.password)
    # user.save()


    # profile = profile_form.save(commit=False)
    # profile.user = user


    # if 'picture' in request.FILES:
    #     profile.picture = request.FILES['picture']

    # profile.save()

    # registered = True

    # else:
    #     print user_form.errors, profile_form.errors

    # else:
    #     user_form = UserForm()
    #     profile_form = UserProfileForm()


    context = {
         
        'profile_form': profile_form, 
        }

    return render(request, './registration/registration_form.html', context)
