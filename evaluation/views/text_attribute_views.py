from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from evaluation.models.evaluation_attribute_model import TextEvaluationAttribute
from evaluation.serializers.evaluation_attribute_serializers import TextEvaluationAttributeSerializer


class TextEvaluationAttributeList(APIView):
    """
    List all TextEvaluationAttributes, or create a new one.
    """

    def get(self, request, school_pk=None, format=None):
        attributes = TextEvaluationAttribute.objects.all()

        # Filter by school
        if school_pk:
            attributes = attributes.filter(school_id=school_pk)

        serializer = TextEvaluationAttributeSerializer(attributes, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TextEvaluationAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TextEvaluationAttributeDetail(APIView):
    """
    Retrieve, update or delete a TextEvaluationAttribute.
    """

    def get_object(self, text_attribute_pk):
        try:
            return TextEvaluationAttribute.objects.get(id=text_attribute_pk)
        except TextEvaluationAttribute.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    def get(self, request, text_attribute_pk, format=None):
        text_attribute = self.get_object(text_attribute_pk)
        serializer = TextEvaluationAttributeSerializer(text_attribute)
        return Response(serializer.data)

    def put(self, request, text_attribute_pk, format=None):
        text_attribute = self.get_object(text_attribute_pk)
        serializer = TextEvaluationAttributeSerializer(
            text_attribute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     # Partially update a specific entry by primary key
    def patch(self, request, text_attribute_pk):
        text_attribute = self.get_object(text_attribute_pk)
        serializer = TextEvaluationAttributeSerializer(
            text_attribute, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, text_attribute_pk, format=None):
        text_attribute = self.get_object(text_attribute_pk)
        text_attribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
