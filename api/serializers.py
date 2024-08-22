# from rest_framework import serializers
# from student.models import Student
# from classperiod.models import ClassPeriod
# from course.models import Course
# from teacher.models import Teacher
# from classroom.models import Classroom


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"


# class ClassPeriodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassPeriod
#         fields = '__all__'

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'


# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = '__all__'

# class ClassroomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classroom
#         fields = '__all__'

from rest_framework import serializers
from student.models import Student
from course.models import Course
from classroom.models import Classroom
from teacher.models import Teacher
from classperiod.models import ClassPeriod
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name= serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields=["id","full_name","email"]
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ["id", "start_time", "end_time"]
class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id", "name", "description"]
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id"]
class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    class Meta:
        model = Teacher
        fields = ["id", "full_name"]
        