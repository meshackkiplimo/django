from django.urls import path
from . import views

#url conf

urlpatterns=[
    path('hello/',views.say_hello),
]