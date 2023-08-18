from rest_framework.response import Response
from rest_framework.decorators import api_view


# GREETING VIEW


@api_view(['GET'])
def helloWorld(request):

    return Response({"message": "Hello World"})
     

