from rest_framework.response import Response
from rest_framework.decorators import api_view
from classes.models import ClassStudent

from classes.serializers import ClassStudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


#
#
#
# CLASS LIST ROUTES
#
#
#


@api_view(['POST'])
def addClassStudent(request):
    serializer = ClassStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def deleteClassStudent(request, class_pk, student_pk):
    classStudent = ClassStudent.objects.filter(class_id=class_pk).filter(student_id=student_pk)
    classStudent.delete()

    return Response({"message": "Student successfully removed from class."})
