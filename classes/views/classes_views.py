from rest_framework.response import Response
from rest_framework.decorators import api_view
from classes.models import ClassEntity
from users.models import User
from classes.serializers import ClassEntitySerializer, ClassEntityWriteSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


class ClassEntityList(APIView):
    """
    List all Classes, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        if school_pk:
            current_class = ClassEntity.objects.filter(school=school_pk)

        else:
            current_class = ClassEntity.objects.all()
        
        serializer = ClassEntitySerializer(current_class, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClassEntityWriteSerializer(data=request.data)
        if serializer.is_valid():
            new_subject_level = serializer.save()
            new_serializer = ClassEntityWriteSerializer(new_subject_level)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(new_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassEntityDetail(APIView):
    """
    Retrieve, update or delete a ClassEntity.
    """

    def get_object(self, class_pk):
        try:
            return ClassEntity.objects.get(id=class_pk)
        except ClassEntity.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, class_pk, format=None):
        current_class = self.get_object(class_pk)
        serializer = ClassEntitySerializer(current_class)
        return Response(serializer.data)

    def put(self, request, class_pk, format=None):
        current_class = self.get_object(class_pk)
        serializer = ClassEntityWriteSerializer(current_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # Partially update a specific entry by primary key
    def patch(self, request, class_pk):
        current_class = self.get_object(class_pk)
        serializer = ClassEntityWriteSerializer(current_class, data=request.data, partial=True)
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
    classes = ClassEntity.objects.filter(school_id=school_pk)
    serializer = ClassEntitySerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def listSchoolTodayClasses(request, school_pk, day_pk):
    today_classes = ClassEntity.objects.filter(school_id=school_pk).filter(day=day_pk)
    serializer = ClassEntitySerializer(today_classes, many=True)

    return Response(serializer.data)

# 
# 
# CLASS-TEACHER ROUTES
# 
# 

@api_view(['PATCH'])
def addClassTeacher(request, class_pk):
    try:
        current_class = ClassEntity.objects.get(id=class_pk)
    except ClassEntity.DoesNotExist:
        return Response({"detail": "ClassEntity not found."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        teacher = User.objects.get(id=request.data['teacher'])
    except User.DoesNotExist:
        return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)
    
    current_class.teacher = teacher
    current_class.save()

    serializer = ClassEntitySerializer(current_class)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def removeClassTeacher(request, class_pk):
    try:
        current_class = ClassEntity.objects.get(id=class_pk)
    except ClassEntity.DoesNotExist:
        return Response({"detail": "ClassEntity not found."}, status=status.HTTP_404_NOT_FOUND)
    
    current_class.teacher = None
    current_class.save()

    serializer = ClassEntitySerializer(current_class)
    return Response(serializer.data, status=status.HTTP_200_OK)
