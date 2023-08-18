from rest_framework.response import Response
from rest_framework.decorators import api_view
from classes.models import Class, ClassStudent
from ..serializers.serializers import ClassSerializer, ClassStudentSerializer

@api_view(['GET'])
def getClasses(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getClassesBySchoolId(request, pk):
    classes = Class.objects.filter(school_id=pk)
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getClassById(request, pk):
    thisClass = Class.objects.get(id=pk)
    serializer = ClassSerializer(thisClass, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def getClassBySchoolAndDate(request, school_pk, date_pk):
    thisClass = Class.objects.filter(school_id=school_pk).filter(day=date_pk)
    serializer = ClassSerializer(thisClass, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getClassesWithClassLists(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addClass(request):
    serializer = ClassSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteClass(request, pk):
    this_class = Class.objects.get(id=pk)
    this_class.delete()

    return Response({"message": "School successfully deleted."})


#
#
#
# CLASS LIST ROUTES
#
#
#


@api_view(['POST'])
def registerStudentInClass(request):
    serializer = ClassStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def removeStudentFromClassStudentById(request, class_pk, student_pk):
    classStudent = ClassStudent.objects.filter(
        class_id=class_pk).filter(student_id=student_pk)
    classStudent.delete()

    return Response({"message": "Student successfully removed from class."})