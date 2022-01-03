from django.urls import path
#import regex
from django.conf.urls import url, include

from myapp import views as myapp_views

from . import views

# for ajax
#from dajaxice.core import dajaxice_autodiscover, dajaxice_config
#dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# for ajax end

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
###########################################################################################################

admin.autodiscover()


urlpatterns = [
    path('',                 myapp_views.TemplateView.as_view(template_name='login.html')),
    url(r'^loginMSI/',       myapp_views.loginMSI,     name='loginMSI'),
    url(r'^loginMSU/',       myapp_views.loginMSU,     name='loginMSU'),
    url(r'^Signup/',         myapp_views.Signup,       name='Signup'),
    url(r'^logout/',         myapp_views.logout,       name = 'logout'),
    url(r'^uploadfile/',     myapp_views.uploadfile,   name='uploadfile'),
    url(r'^fulldataview/',   myapp_views.fulldataview, name='fulldataview'),
    url(r'^welcome_toFP/$',  myapp_views.welcome_toFP, name='welcome_toFP'),
    url(r'^save_changes/$',  myapp_views.save_changes, name='save_changes'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

###############################################################################################################

