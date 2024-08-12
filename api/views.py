from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")
        if first_name:
            students = students.filter(first_name = first_name)

        if country:
            country = students.filter(country = country)

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status = status.HTTP_202_ACCEPTED)

    def enroll_student(self, student, course_id):
        course = Course.objects.get(id = course_id)
        student.courses.add(course)

    def post(self, request_id):
        student = Student.objects.get(id = id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course")
            self.enroll_student(student, course_id)

        return Response(status.HTTP_201_ACCEPTED)
        


class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)

    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ClassroomListView(APIView):
    def get(self , request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many = True)
        return Response(serializer.data)

    
    def post(self , request):
        serializer = ClassroomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classperiod)
        return Response(serializer.data)

    def put(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassPeriodSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classroom = Classroom.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TeacherListView(APIView):
    def get(self , request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many = True)
        return Response(serializer.data)

    
    def post(self , request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseListView(APIView):
    def get(self , request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)

    
    def post(self , request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self,request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(student)
        return Response(serializer.data)

    def put(self,request,id):
        courses = Course.objects.get(id = id)
        serializer = CourseSerializer(courses, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        course = Student.objects.get(id = id)
        course.delete()
        return Response(status = status.HTTP_202_ACCEPTED)

# Create your views here.

