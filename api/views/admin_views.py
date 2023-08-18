from rest_framework.response import Response
from rest_framework.decorators import api_view
from levels.models import Level
from ..serializers.serializers import LevelSerializer


#
#
#
# LEVELS ROUTES
#
#
#


@api_view(['GET'])
def getAllLevels(request):
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getLevelsBySchoolId(request, pk):
    levels = Level.objects.filter(school_id=pk)
    serializer = LevelSerializer(levels, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addLevel(request):
    serializer = LevelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteLevel(request, pk):
    level = Level.objects.get(id=pk)
    level.delete()

    return Response({"message": "Level deleted."})
