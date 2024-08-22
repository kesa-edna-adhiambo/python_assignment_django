# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from student.models import Student
# from .serializers import StudentSerializer

# from .serializers import ClassPeriodSerializer
# from classperiod.models import ClassPeriod

# from .serializers import ClassroomSerializer
# from classroom.models import Classroom

# from .serializers import TeacherSerializer
# from teacher.models import Teacher

# from .serializers import CourseSerializer
# from course.models import Course



# class StudentListView(APIView):

#     def get(self, request):
#         students = Student.objects.all()
#         first_name = request.query_params.get("first_name")
#         country = request.query_params.get("country")
#         if first_name:
#             students = students.filter(first_name = first_name)

#         if country:
#             country = students.filter(country = country)

#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     def post(self, request):

#         serializer = StudentSerializer(data=request.data)  
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def MinnimalSttudentSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Student
#             fields = ["first_name" , "email"]


# class StudentDetailView(APIView):
#     def get(self,request,id):
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self,request,id):
#         student = Student.objects.get(id = id)
#         serializer = StudentSerializer(student, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         student = Student.objects.get(id = id)
#         student.delete()
#         return Response(status = status.HTTP_202_ACCEPTED)

#     def enroll_student(self, student, course_id):
#         course = Course.objects.get(id = course_id)
#         student.courses.add(course)

#     def post(self, request_id):
#         student = Student.objects.get(id = id)
#         action = request.data.get("action")
#         if action == "enroll":
#             course_id = request.data.get("course")
#             self.enroll_student(student, course_id)

#         return Response(status.HTTP_201_ACCEPTED)
        


# class ClassPeriodListView(APIView):
#     def get(self, request):
#         classperiods = ClassPeriod.objects.all()
#         serializer = ClassPeriodSerializer(classperiods, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ClassPeriodSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def MinnimalClassPeriodSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = ClassPeriod
#             fields = ["start_time" , "end_time"]

# class ClassPeriodDetailView(APIView):
#     def get(self, request, id):
#         classperiod = ClassPeriod.objects.get(id=id)
#         serializer = ClassPeriodSerializer(classperiod)
#         return Response(serializer.data)

#     def put(self, request, id):
#         classperiod = ClassPeriod.objects.get(id=id)
#         serializer = ClassPeriodSerializer(classperiod, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         classperiod = ClassPeriod.objects.get(id=id)
#         classperiod.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class ClassroomListView(APIView):
#     def get(self , request):
#         classroom = Classroom.objects.all()
#         serializer = ClassroomSerializer(classroom, many = True)
#         return Response(serializer.data)

    
#     def post(self , request):
#         serializer = ClassroomSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        
#      def MinnimalSttudentSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Student
#             fields = ["first_name" , "email"]

# class ClassroomDetailView(APIView):
#     def get(self, request, id):
#         classroom = Classroom.objects.get(id=id)
#         serializer = ClassroomSerializer(classperiod)
#         return Response(serializer.data)

#     def put(self, request, id):
#         classroom = Classroom.objects.get(id=id)
#         serializer = ClassPeriodSerializer(classroom, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         classroom = Classroom.objects.get(id=id)
#         classperiod.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class TeacherListView(APIView):
#     def get(self , request):
#         teachers = Teacher.objects.all()
#         first_name = request.query_params.get("first_name")
#         subject = request.query_params.get("subject")
#         if first_name:
#            teachers = teachers.filter(first_name = first_name)

#         if subject:
#             subject = teachers.filter(country = country)
#         serializer = TeacherSerializer(teachers, many = True)
#         return Response(serializer.data)

    
#     def post(self , request):
#         serializer = TeacherSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        

#     def MinnimalTeacherSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Teacher
#             fields = ["first_name" , "email"]

# class TeacherDetailView(APIView):
#     def get(self, request, id):
#         teacher = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teacher)
#         return Response(serializer.data)

#     def put(self, request, id):
#         teacher = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(classroom, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         teacher = Teacher.objects.get(id=id)
#         teacher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#     def enroll_teacher(self, teacher, course_id):
#         classroom = Classroom.objects.get(id = classroom_id)
#         teacher.classrooms.add(classroom)

#     def post(self, request_id):
#         teacher =Teacher.objects.get(id = id)
#         action = request.data.get("action")
#         if action == "enroll":
#             classroom_id = request.data.get("classroom")
#             self.enroll_teacher(teacher, classroom_id)

#         return Response(status.HTTP_201_ACCEPTED)


# class CourseListView(APIView):
#     def get(self , request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many = True)
#         return Response(serializer.data)

    
#     def post(self , request):
#         serializer = CourseSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

# class CourseDetailView(APIView):
#     def get(self,request,id):
#         course = Course.objects.get(id=id)
#         serializer = CourseSerializer(student)
#         return Response(serializer.data)

#     def put(self,request,id):
#         courses = Course.objects.get(id = id)
#         serializer = CourseSerializer(courses, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         course = Student.objects.get(id = id)
#         course.delete()
#         return Response(status = status.HTTP_202_ACCEPTED)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from student.models import Student
from course.models import Course
from classroom.models import Classroom
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from .serializers import (
    StudentSerializer, MinimalStudentSerializer,
    CourseSerializer, MinimalCourseSerializer,
    ClassesSerializer, MinimalClassesSerializer,
    TeacherSerializer, MinimalTeacherSerializer,
    ClassPeriodSerializer, MinimalClassPeriodSerializer
)
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = MinimalStudentSerializer
class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = MinimalCourseSerializer
class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class TeacherListView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = MinimalTeacherSerializer
class TeacherDetailView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
class ClassesListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = MinimalClassesSerializer
class ClassDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassesSerializer
class ClassPeriodListView(ListAPIView):
    queryset = ClassPeriod.objects.all()
    serializer_class = MinimalClassPeriodSerializer
class ClassroomPeriodDetailView(RetrieveAPIView):
    queryset = ClassPeriod.objects.all()
    serializer_class = ClassPeriodSerializer
class StudentActionView(APIView):
    def post(self, request, id):
        action = request.data.get('action')
        if action == 'add_to_class':
            return self.add_student_to_class(request, id)
        elif action == 'assign_teacher_course':
            return self.assign_teacher_course(request)
        elif action == 'assign_teacher_class':
            return self.assign_teacher_class(request)
        elif action == 'create_class_period':
            return self.create_class_period(request)
        elif action == 'get_weekly_timetable':
            return self.get_weekly_timetable(request)
        else:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
    def add_student_to_class(self, request, student_id):
        class_id = request.data.get('class_id')
        try:
            student = Student.objects.get(id=student_id)
            class_obj = Classroom.objects.get(id=class_id)
            class_obj.students.add(student)
            return Response({"message": "Student added to class successfully"}, status=status.HTTP_200_OK)
        except (Student.DoesNotExist, Classroom.DoesNotExist):
            return Response({"error": "Student or Class not found"}, status=status.HTTP_404_NOT_FOUND)
    def assign_teacher_course(self, request):
        teacher_id = request.data.get('teacher_id')
        course_id = request.data.get('course_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.get(id=course_id)
            teacher.courses.add(course)
            return Response({"message": "Teacher assigned to course successfully"}, status=status.HTTP_200_OK)
        except (Teacher.DoesNotExist, Course.DoesNotExist):
            return Response({"error": "Teacher or Course not found"}, status=status.HTTP_404_NOT_FOUND)
    def assign_teacher_class(self, request):
        teacher_id = request.data.get('teacher_id')
        class_id = request.data.get('class_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            class_obj = Classroom.objects.get(id=class_id)
            class_obj.teacher = teacher
            class_obj.save()
            return Response({"message": "Teacher assigned to class successfully"}, status=status.HTTP_200_OK)
        except (Teacher.DoesNotExist, Classroom.DoesNotExist):
            return Response({"error": "Teacher or Class not found"}, status=status.HTTP_404_NOT_FOUND)
    def create_class_period(self, request):
        teacher_id = request.data.get('teacher_id')
        course_id = request.data.get('course_id')
        class_id = request.data.get('class_id')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        day_of_week = request.data.get('day_of_week')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.get(id=course_id)
            class_obj = Classroom.objects.get(id=class_id)
            class_period = ClassPeriod.objects.create(
                teacher=teacher,
                course=course,
                class_obj=class_obj,
                start_time=start_time,
                end_time=end_time,
                day_of_week=day_of_week
            )
            serializer = ClassPeriodSerializer(class_period)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Teacher.DoesNotExist, Course.DoesNotExist, Classroom.DoesNotExist):
            return Response({"error": "Teacher, Course, or Class not found"}, status=status.HTTP_404_NOT_FOUND)
    def get_weekly_timetable(self, request):
        class_id = request.data.get('class_id')
        try:
            class_obj = Classroom.objects.get(id=class_id)
            class_periods = ClassPeriod.objects.filter(class_obj=class_obj).order_by('day_of_week', 'start_time')
            timetable = {}
            for period in class_periods:
                day = period.get_day_of_week_display()
                if day not in timetable:
                    timetable[day] = []
                timetable[day].append({
                    'course': period.course.name,
                    'teacher': period.teacher.name,
                    'start_time': period.start_time.strftime('%H:%M'),
                    'end_time': period.end_time.strftime('%H:%M')
                })
            return Response(timetable, status=status.HTTP_200_OK)
        except Classroom.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.

