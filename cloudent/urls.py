from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from basecloud import views as basecloud_views

urlpatterns = [
    # Examples:
    url(r'^$', basecloud_views.home, name='home'),
    url(r'^profile/$', basecloud_views.clients_profile, name='clients_profile'),
    url(r'^create_order/$', basecloud_views.create_order, name='new_order'),
    url(r'^orders/$', basecloud_views.orders_list, name='orders'),
    url(r'^orders_detail/(\d+)/$', basecloud_views.orders_detail, name='orders_detail'),
    url(r'^order_edit/(\d+)/$', basecloud_views.order_edit, name='order_edit'),

    url(r'^accounts/register/$', basecloud_views.register, name='register'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),

    url('', include('registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)