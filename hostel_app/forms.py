from django import forms
from hostel_app.models import Student,Room,Hostel
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

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.filter(room_alloted=False)

class RoomForm(forms.ModelForm):
    class Meta():
        model = Room
        fields = ['hostel','room_num']

class HostelForm(forms.ModelForm):
    class Meta():
        model = Hostel
        fields = ['hostel_name', 'warden','gender','mess']
