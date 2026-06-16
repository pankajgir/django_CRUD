from django.urls import path
from .views import Home , Add_Student,delete_student,update_student

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add-student/',Add_Student.as_view(),name='add-student'),
    path('delete-student/',delete_student.as_view(),name='delete-student'),
    path("edit-student/<int:id>/",update_student.as_view(),name='edit-student')
]
