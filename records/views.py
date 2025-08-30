# Import necessary Django modules
from django.db import models
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.http import HttpResponse
from .models import Student,Teacher, StudentAttendance, TeacherAttendance
from .forms import StudentForm, TeacherForm, StudentAttendanceForm, TeacherAttendanceForm


# Models



# Views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    student_data = [{'student': s, 'fee_balance': s.total_fee - s.fee_paid} for s in students]
    teacher_data = [{'teacher': t, 'salary_balance': t.total_salary - t.salary_obtained} for t in teachers]

    student_attendance = StudentAttendance.objects.all().order_by('-date')[:10]
    teacher_attendance = TeacherAttendance.objects.all().order_by('-date')[:10]

    return render(request, 'dashboard.html', {
        'student_data': student_data,
        'teacher_data': teacher_data,
        'student_attendance': student_attendance,
        'teacher_attendance': teacher_attendance,
    })


@login_required
def add_student(request):
    if request.method == "POST":
        print("📥 Received Data:", request.POST)  # Debugging
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print("✅ Student added successfully!")  # Debugging
            return redirect("dashboard")
        else:
            print("❌ Form validation failed:", form.errors)  # Debugging
    else:       
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


@login_required
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})


@login_required
def add_student_attendance(request):
    if request.method == 'POST':
        form = StudentAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentAttendanceForm()
    return render(request, 'add_student_attendance.html', {'form': form})


@login_required
def add_teacher_attendance(request):
    if request.method == 'POST':
        form = TeacherAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TeacherAttendanceForm()
    return render(request, 'add_teacher_attendance.html', {'form': form})


@login_required
def search(request):
    query = request.GET.get('q', '')

    students = Student.objects.filter(name__icontains=query)
    student_data = [{'student': s} for s in students]

    teachers = Teacher.objects.filter(name__icontains=query)
    teacher_data = [{'teacher': t} for t in teachers]

    return render(request, 'dashboard.html', {
        'student_data': student_data,
        'teacher_data': teacher_data,
        'query': query,
    })


def attendance_dashboard(request):
    return render(request, 'attendance_dashboard.html')



