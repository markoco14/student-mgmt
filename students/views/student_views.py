from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers.serializers import StudentSerializer


from students.models.student import Student

# Create your views here.
class StudentList(APIView):
    """
    List all Units, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        modules = Student.objects.all()

        # Fetch query parameters
        # school = request.query_params.get('school', None)
        # subject = request.query_params.get('subject', None)
        # level = request.query_params.get('level', None)

        # Filter by school
        if school_pk:
            modules = modules.filter(school=school_pk)

        # # Further filter by subject if provided (use subject name)
        # if subject:
        #     modules = modules.filter(subject_level__subject__name=subject)

        # # Further filter by level if provided (use level order)
        # if level:
        #     modules = modules.filter(subject_level__level__order=level)

        serializer = StudentSerializer(modules, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)