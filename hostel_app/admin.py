from django.contrib import admin

# Register your models here.
from hostel_app.models import Student, Hostel, Mess, Room, Course

admin.site.register(Student)
admin.site.register(Hostel)
admin.site.register(Mess)
admin.site.register(Room)
admin.site.register(Course)
