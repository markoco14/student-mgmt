from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from evaluation.models.evaluation_attribute_model import EvaluationAttribute, RangeEvaluationAttribute
from evaluation.serializers.evaluation_attribute_serializers import EvaluationAttributeSerializer, RangeEvaluationAttributeSerializer


class RangeEvaluationAttributeList(APIView):
    """
    List all RangeEvaluationAttributes, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        attributes = RangeEvaluationAttribute.objects.all()

        # Filter by school
        if school_pk:
            attributes = attributes.filter(school_id=school_pk)

        serializer = RangeEvaluationAttributeSerializer(attributes, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RangeEvaluationAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RangeEvaluationAttributeDetail(APIView):
    """
    Retrieve, update or delete a RangeEvaluationAttribute.
    """

    def get_object(self, range_attribute_pk):
        try:
            return RangeEvaluationAttribute.objects.get(id=range_attribute_pk)
        except RangeEvaluationAttribute.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, range_attribute_pk, format=None):
        evaluation_attribute = self.get_object(range_attribute_pk)
        serializer = RangeEvaluationAttributeSerializer(evaluation_attribute)
        return Response(serializer.data)

    def put(self, request, range_attribute_pk, format=None):
        evaluation_attribute = self.get_object(range_attribute_pk)
        serializer = RangeEvaluationAttributeSerializer(
            evaluation_attribute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     # Partially update a specific entry by primary key
    def patch(self, request, range_attribute_pk):
        evaluation_attribute = self.get_object(range_attribute_pk)
        serializer = RangeEvaluationAttributeSerializer(
            evaluation_attribute, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, range_attribute_pk, format=None):
        evaluation_attribute = self.get_object(range_attribute_pk)
        evaluation_attribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
