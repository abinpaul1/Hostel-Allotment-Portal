from django import forms
from hostel_app.models import Student
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': 'Same as your Roll No.',
        }

class StudentForm(forms.ModelForm):
    # room = forms.ModelChoiceField(queryset=Student.objects.filter(room__room_alloted=False))
    class Meta():
        model = Student
        fields = ('student_name','gender','course','room');

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.queryset = Student.objects.filter(room__room_alloted=False)
