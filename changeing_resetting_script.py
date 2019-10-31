import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hostel_management.settings')

import django
django.setup()

from hostel_app.models import Room,Student

def vacate():
    rooms = Room.objects.all()
    for i in rooms:

        i.room_alloted = False;
        i.save()

def allot():
    students = Student.objects.all()

    for s in students:
        hostel = s.room.hostel
        r_num = s.room.room_num
        room = Room.objects.get(hostel=hostel, room_num=r_num)
        room.room_alloted = True
        room.save()

if __name__ == '__main__':
    print("Vacating ......")
    vacate()
    print("Allotin to students ......")
    allot()
    print("Vacated & Alloted")
