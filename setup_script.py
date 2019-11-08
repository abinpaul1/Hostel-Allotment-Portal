import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hostel_management.settings')

import django
django.setup()

from hostel_app.models import Hostel, Mess, Room, Course
from django.contrib.auth.models import User

import random

NUMBER_OF_ROOMS = 5

def add_course():
    course_list = ['Computer Science','Electronics','Mechanical','Civil']
    faculty_list = ['Saidalavi','Santiago','Jayaraj','George Varghese']

    for index,course_name in enumerate(course_list):
        course_code = "A0"+str(index)
        c = Course.objects.get_or_create(course_code=course_code,course_name=course_name,faculty=faculty_list[index])[0]
        c.save()

def add_mess():
    mess_type_list = ['Veg','Non Veg','Continental','North Indian','South Indian','Arabian','Thai','Chinese','Gujarathi']
    contractor_list = ['Babu P Raj','Sandeep Kumar','Geo Vijay','Reshma','Susheela','Al Qatil','Lee Xang','B D Wong','Navaneeth Patel']
    daily_fees = [55,85,102,70,60,125,101,67,97]
    for index in range(len(mess_type_list)):
        m = Mess.objects.get_or_create(mess_type = mess_type_list[index], contractor = contractor_list[index],daily_fees=daily_fees[index])[0]
        m.save()

def add_hostel():
    messes = Mess.objects.all()
    a_hostel = Hostel.objects.get_or_create(hostel_name="A",warden="Johny",gender="M",mess=messes[0])[0]
    b_hostel = Hostel.objects.get_or_create(hostel_name="B",warden="Tommy",gender="M",mess=messes[1])[0]
    mlh_hostel = Hostel.objects.get_or_create(hostel_name="MLH",warden="Salomi",gender="F",mess=messes[2])[0]
    ilh_hostel = Hostel.objects.get_or_create(hostel_name="ILH",warden="Diana",gender="F",mess=messes[3])[0]

    a_hostel.save()
    b_hostel.save()
    mlh_hostel.save()
    ilh_hostel.save()


def add_rooms():
    hostels = Hostel.objects.all()
    for hostel in hostels:
        for i in range(NUMBER_OF_ROOMS):
            room = Room.objects.get_or_create(hostel=hostel, room_num=i+1,room_alloted=False)[0]
            room.save()

if __name__ == '__main__':
    print("Populating")
    add_course()
    add_mess()
    add_hostel()
    add_rooms()
    print("Populated")
    #Adding warden
    user=User.objects.create_user('chief_warden', password='warden@hostels')
    user.save()
    print("Added Warden")
