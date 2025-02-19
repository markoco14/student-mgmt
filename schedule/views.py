from rest_framework.response import Response
from rest_framework.decorators import api_view
from schedule.schedule_serializers import WeekdaySerializer
from schedule.models import Weekday



@api_view(['GET'])
def getWeekdays(request):
    weekdays = Weekday.objects.all().order_by('id')
    serializer = WeekdaySerializer(weekdays, many=True)

    return Response(serializer.data)
