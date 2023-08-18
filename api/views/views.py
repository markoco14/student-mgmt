from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from levels.models import Level
from reports.models import Report, ReportDetails
from students.models import Student
from schools.models import School, SchoolUser
from classes.models import Class, ClassStudent
from users.models import Teacher, User
from ..serializers.serializers import LevelSerializer, ReportDetailsSerializer, ReportSerializer, SchoolUserSerializer, StudentSerializer, SchoolSerializer, TeacherSerializer, UserSerializer, ClassSerializer, ClassStudentSerializer
from django.db.models import Subquery, Prefetch
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.pagination import PageNumberPagination

# GREETING VIEW


@api_view(['GET'])
def helloWorld(request):

    return Response({"message": "Hello World"})
     

#
#
#
# SCHOOL USER ACCESS ROUTES
#
#
#
@api_view(['GET'])
def getSchoolsByUserAccess(request, pk):
    schools = School.objects.filter(school_users__user=pk)
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


#
#
#
# CLASS LIST ROUTES
#
#
#


@api_view(['POST'])
def registerStudentInClass(request):
    serializer = ClassStudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def removeStudentFromClassStudentById(request, class_pk, student_pk):
    classStudent = ClassStudent.objects.filter(
        class_id=class_pk).filter(student_id=student_pk)
    classStudent.delete()

    return Response({"message": "Student successfully removed from class."})

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

#
#
#
# LEVELS ROUTES
#
#
#


@api_view(['GET'])
def getAllLevels(request):
    levels = Level.objects.all()
    serializer = LevelSerializer(levels, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getLevelsBySchoolId(request, pk):
    levels = Level.objects.filter(school_id=pk)
    serializer = LevelSerializer(levels, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addLevel(request):
    serializer = LevelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteLevel(request, pk):
    level = Level.objects.get(id=pk)
    level.delete()

    return Response({"message": "Level deleted."})
