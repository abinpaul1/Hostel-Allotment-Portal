from django.urls import path
from hostel_app import views

app_name = 'hostel_app'

urlpatterns = [
    path('register/',views.reg, name = "reg"),
    path('hostel/',views.HostelList, name = 'hostel-list'),
    path('hostel/<slug:hostel_name>',views.HostelWiseView, name='hostel-details'),
    path('student/',views.StudentList, name='student-list'),
    path('student/<slug:roll_no>',views.StudentView, name='student-details'),
]
