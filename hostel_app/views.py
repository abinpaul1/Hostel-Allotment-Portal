from django.shortcuts import render
from hostel_app import forms

from django.urls import reverse
from hostel_app.models import Student, Hostel, Mess, Room, Course
# Create your views here.

def index(request):
    return render(request,'hostel_app/index.html')


def reg(request):

    registered = False

    if request.method == 'POST':
        student_form = forms.StudentForm(request.POST)

        if student_form.is_valid():

            student = student_form.save(commit=False)
            student.roll_no = student.roll_no.lower()

            b = Room.objects.get(hostel = student.room.hostel , room_num = student.room.room_num)
            b.room_alloted = True;
            b.save()

            student.save()

            registered = True

        else:
            print(student_form.errors)

    else:
        student_form = forms.StudentForm()

    boys_hostel = Hostel.objects.filter(gender="M")
    girls_hostel = Hostel.objects.filter(gender="F")

    return render(request,'hostel_app/reg.html',
                            {'student_form':student_form,
                            'registered':registered,
                            'boys_hostel':boys_hostel,
                            'girls_hostel':girls_hostel})

from django.views import generic

def HostelList(request):
    hostel = Hostel.objects.all()
    context = {
        'hostel_list':hostel,
    }
    return render(request,'hostel_app/hostel_list.html',
                            context=context)

def HostelWiseView(request,hostel_name):
    students = Student.objects.filter(room__hostel__hostel_name=hostel_name)
    count = students.count()
    hostel = Hostel.objects.get(hostel_name=hostel_name)
    context = {
        'students':students,
        'hostel':hostel,
        'num_students': count,
    }
    return render(request,'hostel_app/hostelwise_details.html',
                            context=context)

def StudentList(request):
    student = Student.objects.all()
    context = {
        'student_list':student,
    }
    return render(request,'hostel_app/student_list.html',
                            context=context)

def StudentView(request,roll_no):
    student = Student.objects.get(roll_no = roll_no)
    context = {
        'student':student,
    }
    return render(request,'hostel_app/student_details.html',
                            context=context)
