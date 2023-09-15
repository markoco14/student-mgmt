from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from curriculum.serializers.curriculum_serializers import ModuleSerializer, ModuleTypeSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView



from curriculum.models import Module, ModuleType

    
# 
# MODULE VIEWS
# 

class ModuleList(APIView):
    """
    List all Units, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        modules = Module.objects.all().order_by('order')

        # Fetch query parameters
        # school = request.query_params.get('school', None)
        subject = request.query_params.get('subject', None)
        level = request.query_params.get('level', None)

        # Filter by school
        if school_pk:
            modules = modules.filter(subject_level__subject__school__id=school_pk)

        # Further filter by subject if provided (use subject name)
        if subject:
            modules = modules.filter(subject_level__subject__name=subject)

        # Further filter by level if provided (use level order)
        if level:
            modules = modules.filter(subject_level__level__order=level)

        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModuleDetail(APIView):
    """
    Retrieve, update or delete a Module.
    """

    def get_object(self, module_pk):
        try:
            return Module.objects.get(id=module_pk)
        except Module.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, module_pk, format=None):
        module = self.get_object(module_pk)
        serializer = ModuleSerializer(module)
        return Response(serializer.data)

    def put(self, request, module_pk, format=None):
        module = self.get_object(module_pk)
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, module_pk):
        module = self.get_object(module_pk)
        serializer = ModuleSerializer(module, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, module_pk, format=None):
        module = self.get_object(module_pk)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ModuleTypeList(APIView):
    """
    List all Units, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        modules = ModuleType.objects.all()

        # Fetch query parameters
        # school = request.query_params.get('school', None)
        # subject = request.query_params.get('subject', None)
        # level = request.query_params.get('level', None)

        # Filter by school
        if school_pk:
            modules = modules.filter(school=school_pk)

        # # Further filter by subject if provided (use subject name)
        # if subject:
        #     modules = modules.filter(subject_level__subject__name=subject)

        # # Further filter by level if provided (use level order)
        # if level:
        #     modules = modules.filter(subject_level__level__order=level)

        serializer = ModuleTypeSerializer(modules, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ModuleTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ModuleTypeDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, module_type_pk):
        try:
            return ModuleType.objects.get(id=module_type_pk)
        except ModuleType.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, module_type_pk):
        module_type = self.get_object(module_type_pk)
        serializer = ModuleTypeSerializer(module_type)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, module_type_pk):
        module_type = self.get_object(module_type_pk)
        serializer = ModuleTypeSerializer(module_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, module_type_pk):
        module_type = self.get_object(module_type_pk)
        serializer = ModuleTypeSerializer(module_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, module_type_pk):
        module_type = self.get_object(module_type_pk)
        module_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
