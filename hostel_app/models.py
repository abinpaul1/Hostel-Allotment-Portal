from django.db import models

# Create your models here.
class Student(models.Model):

    roll_no = models.CharField(max_length=50, primary_key=True)
    student_name = models.CharField(max_length=50)

    gender_choice = [('M',"Male"),('F',"Female")]
    gender = models.CharField(choices=gender_choice, max_length=1, default=None)

    course = models.ForeignKey("Course",on_delete=models.CASCADE)
    room = models.ForeignKey("Room",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.student_name

class Hostel(models.Model):

    hostel_name = models.CharField(max_length=5, primary_key=True)
    warden = models.CharField(max_length=50)
    gender_choice = [('M',"Male"),('F',"Female")]

    gender = models.CharField(choices=gender_choice, max_length=1, default=None)
    mess = models.ForeignKey("Mess", on_delete=models.CASCADE)

    def __str__(self):
        return self.hostel_name

class Mess(models.Model):

    mess_type = models.CharField(max_length=50,primary_key=True)
    contractor = models.CharField(max_length=50)
    daily_fees = models.IntegerField()

    def __str__(self):
        return self.mess_type

class Room(models.Model):

    hostel = models.ForeignKey("Hostel", on_delete=models.CASCADE)
    room_num = models.IntegerField()
    room_alloted = models.BooleanField(default=False)

    def __str__(self):
        ret_str = str(self.hostel) + "-" + str(self.room_num)
        return ret_str

class Course(models.Model):

    course_code = models.CharField(max_length=50,primary_key=True)
    course_name = models.CharField(max_length=50)
    year_choice =  [('2016',"2016"),('2017',"2017"),('2018','2018'),('2019','2019')]
    year = models.CharField( choices=year_choice, max_length=50)
    faculty = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name
