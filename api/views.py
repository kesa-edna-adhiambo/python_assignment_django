from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from student.models import Student
from .serializers import StudentSerializer

from .serializers import ClassPeriodSerializer
from classperiod.models import ClassPeriod

from .serializers import ClassroomSerializer
from classroom.models import Classroom

from .serializers import TeacherSerializer
from teacher.models import Teacher

from .serializers import CourseSerializer
from course.models import Course





class StudentListView(APIView):
    def get(self , request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

class ClassPeriodListView(APIView):
    def get(self , request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods, many = True)
        return Response(serializer.data)

class ClassroomListView(APIView):
    def get(self , request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many = True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get(self , request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many = True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self , request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)

# Create your views here.

