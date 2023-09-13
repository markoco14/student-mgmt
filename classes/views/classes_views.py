from rest_framework.response import Response
from rest_framework.decorators import api_view
from classes.models import ClassDay, ClassEntity
from schools.models import SchoolDay
from users.models import User
from classes.serializers import ClassDaySerializer, ClassEntitySerializer, ClassEntityWriteSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


class ClassEntityList(APIView):
    """
    List all Classes, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        class_entity = ClassEntity.objects.all()

        day = request.query_params.get('day', None)

        if school_pk:
            class_entity = class_entity.filter(school=school_pk)

        if day:
            class_entity = class_entity.filter(days__day__day__icontains=day)

        
        serializer = ClassEntitySerializer(class_entity, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        days = request.data['days']
        class_entity_serializer = ClassEntityWriteSerializer(data=request.data)
        if class_entity_serializer.is_valid():
            class_entity = class_entity_serializer.save()
            class_days_to_create = []
            for day in days:
                new_class_day = {
                    "class_id": class_entity.id,
                    "school_day_id": day
                }
                new_class_serializer = ClassDaySerializer(data=new_class_day)
                if not new_class_serializer.is_valid():
                    return Response(new_class_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                class_days_to_create.append(ClassDay(**new_class_serializer.validated_data))
                
            ClassDay.objects.bulk_create(class_days_to_create)
            
            return Response(class_entity_serializer.data, status=status.HTTP_201_CREATED)
        return Response(class_entity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClassEntityDetail(APIView):
    """
    Retrieve, update or delete a ClassEntity.
    """

    def get_object(self, class_entity_pk):
        try:
            return ClassEntity.objects.get(id=class_entity_pk)
        except ClassEntity.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, class_entity_pk, format=None):
        class_entity = self.get_object(class_entity_pk)
        serializer = ClassEntitySerializer(class_entity)
        return Response(serializer.data)

    def put(self, request, class_entity_pk, format=None):
        class_entity = self.get_object(class_entity_pk)
        serializer = ClassEntityWriteSerializer(class_entity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # Partially update a specific entry by primary key
    def patch(self, request, class_entity_pk):
        class_entity = self.get_object(class_entity_pk)
        serializer = ClassEntityWriteSerializer(class_entity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, class_entity_pk, format=None):
        class_entity = self.get_object(class_entity_pk)
        class_entity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)