from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-student/', views.add_student, name='add_student'), 
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('attendance_dashboard/', views.attendance_dashboard, name='attendance_dashboard'),
    path('add_student_attendance/', views.add_student_attendance, name='add_student_attendance'),
    path('add_teacher_attendance/', views.add_teacher_attendance, name='add_teacher_attendance'),
    path('search/', views.search, name='search'),
    #path('add-student/', views.add_student, name='add_student'), 
]
