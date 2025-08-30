from django.db import models
from django import forms


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    fee_paid = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.name} - {self.student_id}"



class Teacher(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    class_handled = models.CharField(max_length=50)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_obtained = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.teacher.name} - {self.date} - {self.status}"


# Forms
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'subject1', 'subject2', 'subject3', 'subject4', 'total_fee', 'fee_paid']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'dob', 'class_handled', 'total_salary', 'salary_obtained']


class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ['student', 'date', 'status']


class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = ['teacher', 'date', 'status']

"""class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    fee_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.student_id}"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    class_handled = models.CharField(max_length=50)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_obtained = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.teacher.name} - {self.date} - {self.status}"


# Forms
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'subject1', 'subject2', 'subject3', 'subject4', 'total_fee', 'fee_paid']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'dob', 'class_handled', 'total_salary', 'salary_obtained']


class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = ['student', 'date', 'status']


class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = ['teacher', 'date', 'status']
"""