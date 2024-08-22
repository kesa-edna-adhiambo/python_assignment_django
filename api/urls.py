from django.urls import path
from .views import StudentListView
from .views import ClassPeriodListView
from .views import TeacherListView
# from .views import ClassroomListView
from .views import CourseListView
from django.contrib import admin
from .views import StudentDetailView
# from .views import ClassPeriodDetailView
# from .views import ClassroomDetailView
from .views import TeacherDetailView
from .views import CourseDetailView




urlpatterns = [
    path('admin/', admin.site.urls),
    path("students/", StudentListView.as_view(), name = "student_list_view"),
    path('classperiods/', ClassPeriodListView.as_view(), name='class_period_list_view'),
    path("teachers/", TeacherListView.as_view(), name = "teacher_list_view"),
    # path("classroom/", ClassroomListView.as_view(), name = "classroom_list_view"),
    path("courses/", CourseListView.as_view(), name = "course_list_view"),
    path("students/<int:id>/", StudentDetailView.as_view(), name = "student_detail_view"),
    path("classperiod/<int:id>/", ClassPeriodListView.as_view(), name = "class_period_list_view"),
    # path("classroom/<int:id>/", ClassroomDetailView.as_view(), name = "classroom_list_view"),
    path("teacher/<int:id>/", TeacherDetailView.as_view(), name = "teacher_list_view"),
    path("course/<int:id>/", CourseDetailView.as_view(), name = "course_list_view"),
    
]
