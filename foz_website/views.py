from django.shortcuts import render, get_object_or_404
from .models import FacultyInfo, Specialty, Department
from datetime import date
from django.shortcuts import render
from .models import ExchangeProgram

def home_view(request):
    info = FacultyInfo.objects.first()
    return render(request, 'faculty/home.html', {'info': info})

def program_list_view(request):
    programs = Specialty.objects.select_related('department').all()
    return render(request, 'faculty/program_list.html', {'programs': programs})

def program_detail_view(request, pk):
    program = get_object_or_404(Specialty.objects.select_related('department'), pk=pk)
    return render(request, 'faculty/program_detail.html', {'program': program})

def department_list_view(request):
    departments = Department.objects.prefetch_related('specialties').all()
    return render(request, 'faculty/department_list.html', {'departments': departments})

def department_detail_view(request, pk):
    department = get_object_or_404(
        Department.objects.prefetch_related('specialties', 'teachers'), pk=pk
    )
    return render(request, 'faculty/department_detail.html', {'department': department})


def exchange_list_view(request):
    programs = ExchangeProgram.objects.all()
    today = date.today()
    return render(request, 'faculty/exchange_list.html', {
        'programs': programs,
        'today': today
    })