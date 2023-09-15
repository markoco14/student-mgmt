from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from curriculum.serializers.curriculum_serializers import SubjectLevelListSerializer, SubjectLevelSerializer, SubjectLevelWriteSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from curriculum.models import SubjectLevel

#
# SUBJECT LEVEL VIEWS
#


class SubjectLevelList(APIView):
    """
    List all SubjectLevels, or create a new one.
    """

    def get(self, request, school_pk=None, subject_pk=None, format=None):
        if school_pk:
            subject_levels = SubjectLevel.objects.filter(
                subject__school__id=school_pk)

            if subject_pk:
                subject_levels = subject_levels.filter(subject__id=subject_pk)

        else:
            subject_levels = SubjectLevel.objects.all()

        serializer = SubjectLevelListSerializer(subject_levels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectLevelWriteSerializer(data=request.data)
        if serializer.is_valid():
            new_subject_level = serializer.save()
            new_serializer = SubjectLevelListSerializer(new_subject_level)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(new_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectLevelDetail(APIView):
    """
    Retrieve, update or delete a SubjectLevel.
    """

    def get_object(self, subject_level_pk):
        try:
            return SubjectLevel.objects.get(id=subject_level_pk)
        except SubjectLevel.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, subject_level_pk, format=None):
        subject_level = self.get_object(subject_level_pk)
        serializer = SubjectLevelSerializer(subject_level)
        return Response(serializer.data)

    def put(self, request, subject_level_pk, format=None):
        subject_level = self.get_object(subject_level_pk)
        serializer = SubjectLevelWriteSerializer(
            subject_level, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     # Partially update a specific entry by primary key
    def patch(self, request, subject_level_pk):
        subject_level = self.get_object(subject_level_pk)
        serializer = SubjectLevelWriteSerializer(
            subject_level, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subject_level_pk, format=None):
        subject_level = self.get_object(subject_level_pk)
        subject_level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
