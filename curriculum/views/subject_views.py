from rest_framework.response import Response
from rest_framework import status
from curriculum.serializers.curriculum_serializers import SubjectSerializer
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from curriculum.models import Subject


class SubjectList(APIView):
    """
    List all Subjects, or create a new one.
    """ 

    def get(self, request, format=None):
        subjects = Subject.objects.all()

        # Fetch query parameters
        per_page = request.query_params.get('per_page', 15)
        page = request.query_params.get('page', None)
        
        school = request.query_params.get('school')
        if school:
            subjects = subjects.filter(school__id=school)
        
        level = request.query_params.get('level', None)
        if level:
            subjects = subjects.filter(levels__level_id=level)
            
        class_id = request.query_params.get('class_id', None)
        if class_id:
            subjects = subjects.filter(levels__level_id__classes__id=class_id)

        if page is not None:

            try:
                page = int(page)
            except ValueError:
                return Response({"detail": "Page number needs to be an integer greater than 0"})
            

            paginator = Paginator(subjects, per_page)

            try:
                subjects = paginator.page(page)
            except PageNotAnInteger:
                subjects = paginator.page(1)
            except EmptyPage:
                subjects = paginator.page(paginator.num_pages)

            serializer = SubjectSerializer(subjects, many=True)

            return Response({
                'count': paginator.count,
                'total_pages': paginator.num_pages,
                'current_page': int(page),
                'per_page': int(per_page),
                'next': subjects.next_page_number() if subjects.has_next() else None,
                'previous': subjects.previous_page_number() if subjects.has_previous() else None,
                'results': serializer.data
            })


        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectDetail(APIView):
    """
    Retrieve, update or delete a Subject.
    """

    def get_object(self, subject_pk):
        try:
            return Subject.objects.get(id=subject_pk)
        except Subject.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, subject_pk, format=None):
        subject = self.get_object(subject_pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, subject_pk, format=None):
        subject = self.get_object(subject_pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # Partially update a specific entry by primary key
    def patch(self, request, subject_pk):
        subject = self.get_object(subject_pk)
        serializer = SubjectSerializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subject_pk, format=None):
        subject = self.get_object(subject_pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)