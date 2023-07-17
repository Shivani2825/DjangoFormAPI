from django.shortcuts import render
from . forms import StudentForm
from .models import StudentData


def home(request):
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            rpassword=fm.cleaned_data['rpassword']
            data=StudentData(name=name,email=email,password=password,rpassword=rpassword)
            data.save()
            fm=StudentForm()
    else:
        fm=StudentForm()
    return render(request,'enroll.html', {'form':fm})
