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

    return Response({"message": "Level deleted."})


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