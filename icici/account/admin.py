from django.contrib import admin
from .models import emp,saving

# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display = ['dept_name','dept_city','dept_id']
class savingadmin(admin.ModelAdmin):
    list_display = ['dept_name','dept_city']

admin.site.register(emp,empadmin)
admin.site.register(saving,savingadmin)