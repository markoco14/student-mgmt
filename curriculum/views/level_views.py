from rest_framework.response import Response
from rest_framework import status
from curriculum.serializers.curriculum_serializers import LevelSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from curriculum.models import Level


class LevelList(APIView):
    """
    List all Levels, or create a new one.
    """ 

    def get(self, request, school_pk=None, format=None):
        levels = Level.objects.all().order_by('order')

        # Fetch query parameters
        per_page = request.query_params.get('per_page', 15)
        page = request.query_params.get('page', None)

        # Filter by school
        if school_pk:
            levels = levels.filter(school__id=school_pk)

        if page is not None:

            try:
                page = int(page)
            except ValueError:
                return Response({"detail": "Page number needs to be an integer greater than 0"})
            

            paginator = Paginator(levels, per_page)

            try:
                levels = paginator.page(page)
            except PageNotAnInteger:
                levels = paginator.page(1)
            except EmptyPage:
                levels = paginator.page(paginator.num_pages)

            serializer = LevelSerializer(levels, many=True)

            return Response({
                'count': paginator.count,
                'total_pages': paginator.num_pages,
                'current_page': int(page),
                'per_page': int(per_page),
                'next': levels.next_page_number() if levels.has_next() else None,
                'previous': levels.previous_page_number() if levels.has_previous() else None,
                'results': serializer.data
            })


        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LevelDetail(APIView):
    """
    Retrieve, update or delete a Level.
    """

    def get_object(self, level_pk):
        try:
            return Level.objects.get(id=level_pk)
        except Level.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, level_pk, format=None):
        level = self.get_object(level_pk)
        serializer = LevelSerializer(level)
        return Response(serializer.data)

    def put(self, request, level_pk, format=None):
        level = self.get_object(level_pk)
        serializer = LevelSerializer(level, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # Partially update a specific entry by primary key
    def patch(self, request, level_pk):
        level = self.get_object(level_pk)
        serializer = LevelSerializer(level, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, level_pk, format=None):
        level = self.get_object(level_pk)
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)