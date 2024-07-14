from django.shortcuts import render

from rest_framework.views import APIView
from classperiod.models import ClassPeriod
from .serializers import StudentSerializer
from rest_framework.response import Response


class ClassPeriodListView(APIView):
    def get(self , request):
        classperiod = ClassPeriod.objects.all()
        serializer = StudentSerializer(classperiod, many = True)
        return Response(serializer.data)

# Create your views here.
