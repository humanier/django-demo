from django.urls import path
from . import views

urlpatterns = [
    path('healthcheck', views.healthcheck, name='healthcheck'),
    path('student', views.create_student, name='create_student'),
    path('student/<int:student_id>', views.get_student, name='get_student'),
    path('student', views.get_students, name='get_students')
]
