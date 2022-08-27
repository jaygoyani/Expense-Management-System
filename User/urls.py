from django.conf.urls import url
from django.views.generic import TemplateView
# from User import views
from . import views


urlpatterns = [

    url('userexpense1/',views.userexpense1),
    url('userexpensedel/',views.userexpensedel),
    url('chart/',views.chart),
    url('chart1/',views.chart1),
    url('profile/', views.profile),
    url('update/', views.update),
    # url('updatet/', views.updatet),
    url('',views.userexpense),
]