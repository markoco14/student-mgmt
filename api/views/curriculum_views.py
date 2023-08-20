from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from api.serializers.curriculum_serializers import SubjectSerializer
from api.serializers.curriculum_serializers import LevelSerializer

from curriculum.models import Level, Subject

#
# LEVELS ROUTES
#

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    
    def get_queryset(self):
        school_pk = self.request.GET.get('school', None)
        if school_pk:
            return Level.objects.filter(school=school_pk)
        
        return super().get_queryset()
    
    # create, update, and destroy functions implied

#
# SUBJECTS ROUTES
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
