from django.urls import path

from .views import *

urlpatterns = [
	path('', RegisterUser.as_view(), name='home'),
	path('login', LoginUser.as_view(), name='login'),
	path('questions/<int:value>', questions, name='questions'),
	path('ready', ready, name='ready'),
	path('questions/<int:value>/yes', yes, name='yes'),
	path('questions/<int:value>/no', no, name='no'),
]