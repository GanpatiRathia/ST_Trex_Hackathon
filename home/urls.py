from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView
from home.dash_apps.finished_apps import simpleexample,regression,regression1

urlpatterns = [
    #path('', views.home, name='home'),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('welcome/', views.welcome, name='welcome'),
    path('graphs/', views.graphs, name='graphs'),
    path('index/', views.index, name='index'),
    path('regression/', views.regression, name='regression'),
    path('regression1/', views.regression1, name='regression1'),
    path('logout/', LogoutView.as_view(), name='logout'),
]