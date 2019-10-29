from django.urls import path
from hostel_app import views

app_name = 'hostel_app'

urlpatterns = [
    path('register/',views.reg,name = "reg"),
]
