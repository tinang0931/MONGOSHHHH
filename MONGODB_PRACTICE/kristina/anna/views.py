# school_inventory/views.py

from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import *

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # Redirect to the student list page
    else:
        form = StudentForm()
    
    return render(request, 'list.html', {'form': form})

def show_list(request):
    s = Student.objects.all()
    context = {
        's':s
    }
    return render(request, 'item.html', context)