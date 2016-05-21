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
		title = 'My profile' #'You are logged in as %s' %(request.user)
		photo = '/static/img/All_OSs.jpg'
		context = {
			"title": title,
			"photo": photo,
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


def orders_detail(request, slug=None):
    instance = get_object_or_404(CustomersOrder, pk=1)
    # if instance.publish > timezone.now().date():
    #     if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    # share_string = quote_plus(instance.content)
    # title = CustomersOrder.title()
    context = {
        "title": instance.title,
        "image": instance.image,
        # "instance": instance,
        # "share_string": share_string,
    }
    return render(request, "orders_detail.html", context)

def orders_list(request):
    # today = timezone.now().date()
    # queryset_list = Post.objects.active() #.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = CustomersOrder.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(queryset_list, 2) #  Show 25 contacts per page
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