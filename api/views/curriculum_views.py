from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
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

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    def get_queryset(self):
        school_pk = self.request.GET.get('school', None)
        if school_pk:
            return Subject.objects.filter(school=school_pk)
        
        return super().get_queryset()
    
    # create, update, and destroy functions implied
