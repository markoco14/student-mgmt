from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from reports.models import Report, ReportDetails
from classes.models import ClassStudent
from ..serializers.serializers import ReportDetailsSerializer, ReportSerializer
from django.core.exceptions import ObjectDoesNotExist

#
#
#
# REPORT ROUTES
#
#
#


@api_view(['GET'])
def getReportsAll(request):
    reports = Report.objects.all()
    serializer = ReportSerializer(reports, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getReportByClassAndDate(request, class_pk, date_pk):
    try:
        report = Report.objects.get(class_id=class_pk, date=date_pk)
        serializer = ReportSerializer(report, many=False)

        return Response(serializer.data)
    except ObjectDoesNotExist:

        return Response({})


@api_view(['GET'])
def getTodayReportByStudentId(request, pk):
    startdate = date.today()
    enddate = startdate + timedelta(days=1)

    report = Report.objects.filter(student_id=pk).filter(
        created_at__gte=startdate).filter(created_at__lt=enddate)
    serializer = ReportSerializer(report, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createReportAndReportDetails(request):
    report_serializer = ReportSerializer(data=request.data)
    if report_serializer.is_valid():
        report_serializer.save()

    print('report id', report_serializer.data['id'])
    class_list = ClassStudent.objects.filter(class_id=report_serializer.data['class_id'])
    for student in class_list:
        print('student id', student.student_id.id)
        details_data = {
            "report": report_serializer.data['id'],
            "student": student.student_id.id
        }
        details_serializer = ReportDetailsSerializer(data=details_data)
        if details_serializer.is_valid():
            details_serializer.save()
        
    return Response(report_serializer.data)


# @api_view(['POST'])
# def updateReport(request, pk):
#     report = Report.objects.get(id=pk)
#     serializer = ReportSerializer(instance=report, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


@api_view(['DELETE'])
def deleteReport(request, pk):
    report = Report.objects.get(id=pk)
    report.delete()

    return Response({"message": "Report successfully deleted."})


#
#
#
# REPORT DETAILS ROUTES
#
#
#
@api_view(['GET'])
def getReportsDetailsByReportId(request, report_pk):
    reportDetails = ReportDetails.objects.filter(
        report=report_pk).prefetch_related('student')
    serializer = ReportDetailsSerializer(reportDetails, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createReportDetails(request):
    serializer = ReportDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    else:

        return Response({'message': 'something went wrong'})


@api_view(['DELETE'])
def deleteReportDetails(request, pk):
    reportDetails = ReportDetails.objects.get(id=pk)
    reportDetails.delete()

    return Response({"message": "Report details deleted"})


@api_view(['PUT'])
def updateReportDetails(request, pk):
    reportDetail = ReportDetails.objects.get(id=pk)
    serializer = ReportDetailsSerializer(
        reportDetail, request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)