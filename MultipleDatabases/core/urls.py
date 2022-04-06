from django.contrib import admin
from django.urls import path,include
from . views import *
urlpatterns = [
  path('add_customer/',AddCustomer.as_view(),name="add_customer"),
  path('customer/',Customer.as_view(),name="customer"),
  path('user_details/',UserDetails.as_view(),name="user_details")

  
]