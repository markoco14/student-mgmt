from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers.curriculum_serializers import SubjectSerializer
from api.serializers.curriculum_serializers import LevelSerializer

from curriculum.models import Level, Subject

#
#
# LEVELS ROUTES
#
#


@api_view(['GET'])
def listSchoolLevels(request, school_pk):
    levels = Level.objects.filter(school_id=school_pk)
    serializer = LevelSerializer(levels, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addLevel(request):
    serializer = LevelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteLevel(request, level_pk):
    level = Level.objects.get(id=level_pk)
    level.delete()

    return Response({"detail": "Level deleted."})


#
#
# SUBJECTS ROUTES
#
#

@api_view(['GET'])
def listSchoolSubjects(request, school_pk):
    subjects = Subject.objects.filter(school=school_pk)
    serializer = SubjectSerializer(subjects, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addSubject(request):
    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSubject(request, subject_pk):
    subject = Subject.objects.get(id=subject_pk)
    subject.delete()

    return Response({"detail": "Subject deleted."})

@api_view(['PATCH'])
def updateSubject(request, subject_pk):
    subject = Subject.objects.get(id=subject_pk)
    serializer = SubjectSerializer(instance=subject, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
