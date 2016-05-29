from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'basecloud.views.home', name='home'),
    url(r'^profile/$', 'basecloud.views.clients_profile', name='clients_profile'),
<<<<<<< HEAD
    url(r'^create_order/$', 'basecloud.views.create_order', name='new_order'),
    url(r'^orders/$', 'basecloud.views.orders_list', name='orders'),
    url(r'^orders_detail/$', 'basecloud.views.orders_detail', name='orders_detail'),

=======
>>>>>>> 9ea45164b2351436dd4f9e000e732492dee96185

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)