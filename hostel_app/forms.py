from django import forms
from hostel_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('roll_no','student_name','gender','course','room');

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Student.objects.filter(room__room_alloted=False)
