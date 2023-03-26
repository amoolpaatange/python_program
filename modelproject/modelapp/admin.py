from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll','name','email','date','mobile','per','year_in_school','test']


admin.site.register(Student,StudentAdmin)


