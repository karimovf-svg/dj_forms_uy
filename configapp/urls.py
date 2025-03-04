from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='home'),
    path('fan/<int:fan_id>', fanlar_new, name='fanlar_new'),
    path('add-subject/', add_subject, name='add_subject'),
    path('add-student/', add_student, name='add_student'),
    path('app/delete/<int:student_id>/', student_del, name='student_del'),
    path('student/<int:student_id>/download/', generate_student_pdf, name='download_student_pdf'),
]
