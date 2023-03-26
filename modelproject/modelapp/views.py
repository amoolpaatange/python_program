from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,FeedbackModel
# Create your views here.
from .forms import FeedbackForm
def show_student(r):
    stud_list = Student.objects.all() # ORM query fetch all rows from tables(database)
    print(stud_list)
    my_dict = {'stud_list':stud_list}
    return render(r,'modelapp/studentform.html',context=my_dict)
def show_feedback(r):
    stud_list = FeedbackModel.objects.all() # ORM query fetch all rows from tables(database)
    print(stud_list)
    my_dict = {'stud_list':stud_list}
    return render(r,'modelapp/show_fd.html',context=my_dict)

def feedback_show(r):
    form = FeedbackForm()
    if r.method=='POST':
        form = FeedbackForm(r.POST)
        if form.is_valid():
            form.save()
            return  HttpResponse('<h1> thanks you </h1>')

    stud_list = FeedbackModel.objects.all()  # ORM query fetch all rows from tables(database)
    print(stud_list)
    my_dict = {'stud_list': stud_list,'form':form}
    return render(r,'modelapp/feedback.html',context=my_dict)


