from rest_framework.response import Response
from rest_framework.decorators import api_view
from classes.models import Class, ClassStudent
from users.models import User
from .serializers import ClassSerializer, ClassStudentSerializer, ClassWriteSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


class ClassList(APIView):
    """
    List all Classes, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        if school_pk:
            current_class = Class.objects.filter(school=school_pk)

        else:
            current_class = Class.objects.all()
        
        serializer = ClassSerializer(current_class, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClassWriteSerializer(data=request.data)
        if serializer.is_valid():
            new_subject_level = serializer.save()
            new_serializer = ClassWriteSerializer(new_subject_level)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(new_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassDetail(APIView):
    """
    Retrieve, update or delete a Class.
    """

    def get_object(self, class_pk):
        try:
            return Class.objects.get(id=class_pk)
        except Class.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, class_pk, format=None):
        current_class = self.get_object(class_pk)
        serializer = ClassSerializer(current_class)
        return Response(serializer.data)

    def put(self, request, class_pk, format=None):
        current_class = self.get_object(class_pk)
        serializer = ClassWriteSerializer(current_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # Partially update a specific entry by primary key
    def patch(self, request, class_pk):
        current_class = self.get_object(class_pk)
        serializer = ClassWriteSerializer(current_class, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, class_pk, format=None):
        current_class = self.get_object(class_pk)
        current_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# OTHER CLASS VIEWS


@api_view(['GET'])
def listSchoolClasses(request, school_pk):
    classes = Class.objects.filter(school_id=school_pk)
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def listSchoolTodayClasses(request, school_pk, day_pk):
    today_classes = Class.objects.filter(school_id=school_pk).filter(day=day_pk)
    serializer = ClassSerializer(today_classes, many=True)

    return Response(serializer.data)

# 
# 
# CLASS-TEACHER ROUTES
# 
# 

@api_view(['PATCH'])
def addClassTeacher(request, class_pk):
    try:
        current_class = Class.objects.get(id=class_pk)
    except Class.DoesNotExist:
        return Response({"detail": "Class not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        teacher = User.objects.get(id=request.data['teacher'])
    except User.DoesNotExist:
        return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)
    
    current_class.teacher = teacher
    current_class.save()

    serializer = ClassSerializer(current_class)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def removeClassTeacher(request, class_pk):
    try:
        current_class = Class.objects.get(id=class_pk)
    except Class.DoesNotExist:
        return Response({"detail": "Class not found."}, status=status.HTTP_404_NOT_FOUND)
    
    current_class.teacher = None
    current_class.save()

    serializer = ClassSerializer(current_class)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
