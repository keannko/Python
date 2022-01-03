from django.urls import  path
from .views import *



urlpatterns = [
    	path('', main_page, name='home'),
    	path('phones/<int:p_id>/', index, name='phone'),
]