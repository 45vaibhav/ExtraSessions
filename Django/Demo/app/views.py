from django.shortcuts import render
from .serilizers import StudentSerilizer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def add_student(request):
    student=StudentSerilizer(data=request.data)
    if student.is_valid():
         student.save()
   
         return Response({
        "msg":"it works added "
         })
    return Response({
        "msg":"not added "
    })     
    
@api_view(["GET"])

def all_students(request):
    students=Student.objects.all()
    students=StudentSerilizer(students,many=True)
    print("all students")
    return Response(
        students.data
    )
    
@api_view(["DELETE"])

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return Response({
        "msg":"student deleted successfully"
   } )
    

