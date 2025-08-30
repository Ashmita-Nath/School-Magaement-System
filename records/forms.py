from django import forms
from .models import StudentAttendance, TeacherAttendance, Student, Teacher

class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ['student', 'date', 'status']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = ['teacher', 'date', 'status']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'subject1', 'subject2', 'subject3', 'subject4', 'total_fee', 'fee_paid']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'dob', 'class_handled', 'total_salary', 'salary_obtained']