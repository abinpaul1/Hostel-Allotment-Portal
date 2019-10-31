from django.urls import path
from hostel_app import views

app_name = 'hostel_app'

urlpatterns = [
    path('user_login/',views.user_login, name='user_login'),
    path('register/',views.reg, name = "reg"),
    path('hostel/',views.HostelList, name = 'hostel-list'),
    path('hostel_details/',views.HostelWiseView, name='hostel-details'),
    # path('hostel/<slug:username>',views.HostelRedirectView, name='hostel-details-redirect'),
    path('student_list/',views.StudentList, name='student-list'),
    path('hostel/student_list/',views.HostelStudentList, name='hostel-student-list'),
    path('profile/',views.StudentProfileView, name='student-details'),
    path('profile/edit',views.edit, name='edit-profile'),
]
