from typing import List
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers.serializers import StudentSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from classes.models import ClassEntity
from evaluation.models.evaluation_attribute_model import EvaluationAttribute, RangeEvaluationAttribute
from evaluation.models.student_evaluation_model import StudentEvaluation
from students.models.student import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.serializers.student_evaluation_serializers import StudentWithEvaluationSerializer

# Create your views here.


def get_augmented_evaluation_attributes(school_id: int):
    evaluation_attributes = EvaluationAttribute.objects.filter(
        school_id=school_id).prefetch_related('rangeevaluationattribute', 'textevaluationattribute')

    for attribute in evaluation_attributes:
        range_attr = getattr(attribute, 'rangeevaluationattribute', None)
        if range_attr:
            attribute.max_value = range_attr.max_value
        # If additional processing for text_attr or other types is needed, add here.
    return evaluation_attributes


def prepare_evaluation_records_for_students(students, evaluation_attributes, author_id, date, class_id, subject_id, level_id):
    # CREATE HOLDER FOR EVALUATION RECORDS
    evaluation_records = []

    for student in students:
        if not student['evaluations_for_day']:
            for attribute in evaluation_attributes:
                range_attr = getattr(
                    attribute, 'rangeevaluationattribute', None)
                if range_attr:
                    evaluation_record = {
                        "evaluation_type": 0,
                        "student_id_id": student['id'],
                        "author_id_id": author_id,
                        "date": date,
                        "evaluation_attribute_id_id": attribute.id,
                        "evaluation_value": str(range_attr.max_value),
                        "class_id_id": class_id,
                        "subject_id_id": subject_id,
                        "level_id_id": level_id,
                    }
                else:
                    evaluation_record = {
                        "evaluation_type": 0,
                        "student_id_id": student['id'],
                        "author_id_id": author_id,
                        "date": date,
                        "evaluation_attribute_id_id": attribute.id,
                        "evaluation_value": "",
                        "class_id_id": class_id,
                        "subject_id_id": subject_id,
                        "level_id_id": level_id,
                    }

                evaluation_records.append(evaluation_record)

    return evaluation_records


@api_view(['POST'])
def create_evaluation_records_for_class_list(request):
    students: List[Student] = request.data['students']
    class_id: int = request.data['class_id']
    author_id: int = request.data['user_id']
    date: str = request.data['date']
    school_id: int = request.data['school_id']

    subject_id = request.data['subject_id']

    level = ClassEntity.objects.get(id=class_id).level

    evaluation_attributes = get_augmented_evaluation_attributes(
        school_id=school_id)

    evaluation_records = prepare_evaluation_records_for_students(
        students=students,
        evaluation_attributes=evaluation_attributes,
        author_id=author_id,
        date=date,
        class_id=class_id,
        subject_id=subject_id,
        level_id=level.id)

    created_records = StudentEvaluation.objects.bulk_create(
        [StudentEvaluation(**record) for record in evaluation_records])

    if created_records:
        # BECAUSE BATCH CREATE RETURNING NULL IDS = FRONTEND RENDERING PROBLEM
        # SO RE-FETCH STUDENTS WITH NEW EVALUATION RECORDS
        fetched_records = Student.objects.filter(class_students__class_id=class_id,
                                                 attendance__class_id=class_id, attendance__status__in=[0, 1]).order_by('last_name')
        serializer = StudentWithEvaluationSerializer(
            fetched_records, many=True, context={'class_entity': class_id, 'date': date})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'detail': 'Attendance records created'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_students_with_evaluations(request, school_pk=None):
    students = Student.objects.all().order_by('last_name')

    class_entity = request.query_params.get('class_entity', None)
    date = request.query_params.get('date', None)
    present = request.query_params.get('present', None)

    if class_entity:
        students = students.filter(class_students__class_id=class_entity)

    if present:
        students = students.filter(
            attendance__class_id=class_entity,
            attendance__date=date,
            attendance__status__in=[0, 1],)

    # DUPLICATES DUE TO QUERY
    students = students.distinct()

    serializer = StudentWithEvaluationSerializer(
        students, many=True, context={'class_entity': class_entity, 'date': date})

    return Response(serializer.data)


class StudentList(APIView):
    """
    List all Units, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        students = Student.objects.all().order_by('last_name')

        # Fetch query parameters
        first_name = request.query_params.get('first_name', None)
        last_name = request.query_params.get('last_name', None)
        age = request.query_params.get('age', None)
        gender = request.query_params.get('gender', None)

        class_entity = request.query_params.get('class_entity', None)

        # FOR PAGES BASED ON ATTENDANCE
        attendance = request.query_params.get('attendance', None)
        date = request.query_params.get('date', None)

        page = request.query_params.get('page', None)
        per_page = request.query_params.get('per_page', 15)

        # Filter by school (hierachical url)
        if school_pk:
            students = students.filter(school_id=school_pk)

        # Further filter by query params
        if first_name:
            students = students.filter(first_name=first_name)
        if last_name:
            students = students.filter(last_name=last_name)
        if age:
            students = students.filter(age=age)
        if gender:
            students = students.filter(gender=gender)

        if class_entity:
            students = students.filter(class_students__class_id=class_entity)

        if attendance and date:
            students = students.filter(attendance__status__in=[
                                       0, 1]).filter(attendance__date=date)

        # check if page number is letters and send response that can be alerted
        # even though the front end should control for this.

        if page is not None:

            try:
                page = int(page)
            except ValueError:
                return Response({"detail": "Page number needs to be an integer greater than 0"})

            paginator = Paginator(students, per_page)

            try:
                students = paginator.page(page)
            except PageNotAnInteger:
                students = paginator.page(1)
            except EmptyPage:
                students = paginator.page(paginator.num_pages)

            serializer = StudentSerializer(students, many=True)

            return Response({
                'count': paginator.count,
                'total_pages': paginator.num_pages,
                'current_page': int(page),
                'per_page': int(per_page),
                'next': students.next_page_number() if students.has_next() else None,
                'previous': students.previous_page_number() if students.has_previous() else None,
                'results': serializer.data
            })

        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, student_pk):
        try:
            return Student.objects.get(id=student_pk)
        except Student.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, student_pk):
        student = self.get_object(student_pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, student_pk):
        student = self.get_object(student_pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, student_pk):
        student = self.get_object(student_pk)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, student_pk):
        student = self.get_object(student_pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
