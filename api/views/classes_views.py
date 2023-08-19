from rest_framework.response import Response
from rest_framework.decorators import api_view
from classes.models import Class, ClassStudent
from users.models import User
from ..serializers.serializers import ClassSerializer, ClassStudentSerializer
from rest_framework import status


# CLASS MODEL CRUD VIEWS

@api_view(['GET'])
def listClasses(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getClassById(request, class_pk):
    thisClass = Class.objects.get(id=class_pk)
    serializer = ClassSerializer(thisClass, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def addClass(request):
    serializer = ClassSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteClass(request, class_pk):
    this_class = Class.objects.get(id=class_pk)
    this_class.delete()

    return Response({"message": "School successfully deleted."})

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
