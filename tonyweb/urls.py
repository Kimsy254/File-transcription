"""tonyweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from paypal.standard.ipn import urls as paypal_urls
from django.urls import path, include
from . import views
from upload import views as upload_views
from paypal_store import views as paypal_views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "Tony Web"
admin.site.site_title = "Tony Web Portal"
admin.site.index_title = "Welcome to Tony Web Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name="home"),
    path('accounts/', include('accounts.urls')),
     # Upload
    path('uploadfiles/', upload_views.get_upload_file_form, name='uploadfiles'),
    url(r'^transcriptdetails', upload_views.get_transcript_detail_form, name='transcriptdetails'),
    url(r'^removefile/(?P<upload_id>\d+)/$', upload_views.remove_file, name='removefile'),
    url(r'^orderreview', upload_views.get_order_review, name='orderreview'),
    url(r'^save-to-cart/(?P<detail_id>\d+)/$', upload_views.save_to_cart, name='save_to_cart'),
    url(r'^my-cart/$', upload_views.get_my_cart, name='my_cart'),
    url(r'^transcript-tracker/$', upload_views.get_transcript_tracker, name='transcript_tracker'),
    url(r'^transcript-tracker/new/(?P<detail_id>\d+)/$', upload_views.new_review, name='new_review'),
    url(r'^transcript-tracker/edit/(?P<detail_id>\d+)/(?P<review_id>\d+)/$', upload_views.edit_review, name='edit_review'),

    # Paypal Store
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('paypal-notification/', include(paypal_urls)),
    path('paypal-return', paypal_views.paypal_return, name='paypal-return'),
    path('paypal-cancel', paypal_views.paypal_cancel, name='paypal-cancel'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)