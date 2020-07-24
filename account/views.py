from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        print(request)
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration Successfull!')
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request,'account/register.html',{'form':form})

# def login(request):
#     pass
