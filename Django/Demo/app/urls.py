from django.urls import path
from .views import add_student,all_students,delete_student
urlpatterns = [
    path("addstudent/",add_student),
    path("allstudents/",all_students),
    path("deletestudent/<int:id>",delete_student)
]
