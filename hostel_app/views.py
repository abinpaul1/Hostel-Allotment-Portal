from django.shortcuts import render, redirect
from hostel_app import forms

from django.urls import reverse
from hostel_app.models import Student, Hostel, Mess, Room, Course
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

def index(request):
    return render(request,'hostel_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def reg(request):

    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        student_form = forms.StudentForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)  #For hashing passwords
            user.save()

            student = student_form.save(commit=False)
            student.user = user;

            b = Room.objects.get(hostel = student.room.hostel , room_num = student.room.room_num)
            b.room_alloted = True;
            b.save()

            student.save()
            registered = True

        else:
            print(user_form.errors , student_form.errors)

    else:
        user_form = forms.UserForm()
        student_form = forms.StudentForm()

    boys_hostel = Hostel.objects.filter(gender="M")
    girls_hostel = Hostel.objects.filter(gender="F")

    return render(request,'hostel_app/reg.html',
                            {'user_form':user_form,
                            'student_form':student_form,
                            'registered':registered,
                            'boys_hostel':boys_hostel,
                            'girls_hostel':girls_hostel})


@login_required
def edit(request):
    current_student = Student.objects.get(user__username=request.user.get_username())
    current_hostel = current_student.room.hostel.hostel_name
    current_room = current_student.room.room_num
    if request.method == 'POST':
        #Deallocating current room
        b = Room.objects.get(hostel = current_hostel , room_num = current_room)
        b.room_alloted = False;
        b.save()

        student_form = forms.StudentForm(request.POST, instance=request.user.student)
        if student_form.is_valid():
            current_student = Student.objects.get(user__username=request.user.get_username())
            current_hostel = current_student.room.hostel.hostel_name
            current_room = current_student.room.room_num

            student = student_form.save(commit=False)

            #Allocating new room
            b = Room.objects.get(hostel = student.room.hostel , room_num = student.room.room_num)
            b.room_alloted = True;
            b.save()

            student.save()
            return render(request, 'hostel_app/index.html')
        else:
            #Re-allocating current room
            b = Room.objects.get(hostel = current_hostel , room_num = current_room)
            b.room_alloted = True;
            b.save()
    else:
        student_form = forms.StudentForm(instance=request.user.student)

    boys_hostel = Hostel.objects.filter(gender="M")
    girls_hostel = Hostel.objects.filter(gender="F")

    return render(request,'hostel_app/profile_edit.html',
                            {'student_form':student_form,
                            'boys_hostel':boys_hostel,
                            'girls_hostel':girls_hostel})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,'hostel_app/login.html')

from django.views import generic

def HostelList(request):
    hostel = Hostel.objects.all()
    context = {
        'hostel_list':hostel,
    }
    return render(request,'hostel_app/hostel_list.html',
                            context=context)

@login_required
def HostelWiseView(request):
    current_student = Student.objects.get(user__username=request.user.get_username())
    hostel_name = current_student.room.hostel.hostel_name
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

@login_required
def HostelStudentList(request):
    current_student = Student.objects.get(user__username=request.user.get_username())
    hostel_name = current_student.room.hostel.hostel_name
    students = Student.objects.filter(room__hostel__hostel_name=hostel_name)
    context = {
        'student_list':students,
    }
    return render(request,'hostel_app/hostel_student_list.html',
                            context=context)

@login_required
def StudentProfileView(request):
    current_user = request.user.get_username()
    student = Student.objects.get(user__username = current_user)
    context = {
        'student':student,
    }
    return render(request,'hostel_app/student_details.html',
                            context=context)
