from django.conf.urls import url, include
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from . import views
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url('contact/',views.contact),
    url('about/',views.about),
    url('',views.home),

]