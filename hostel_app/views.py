from django.shortcuts import render
from hostel_app import forms

from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,'hostel_app/index.html')


def reg(request):

    registered = False

    if request.method == 'POST':
        student_form = forms.StudentForm(request.POST)

        if student_form.is_valid():

            student = student_form.save(commit=False)

            student.save()

            registered = True

        else:
            print(student_form.errors)

    else:
        student_form = forms.StudentForm()

    return render(request,'hostel_app/reg.html',
                            {'student_form':student_form,
                            'registered':registered})
