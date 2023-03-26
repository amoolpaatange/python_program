from django.shortcuts import render
from django.http import HttpResponse
from .models import emp,saving
# Create your views here.
def show1(r):
      prd=emp.objects.all()
      prd1 = saving.objects.all()
      md={'prd_list':prd,'prd_list1':prd1}
      return render(r,'index.html',context=md)
# Create your views here.
