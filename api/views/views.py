from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from levels.models import Level
from reports.models import Report, ReportDetails
from students.models import Student
from schools.models import School, SchoolUser
from classes.models import Class, ClassStudent
from users.models import Teacher, User
from ..serializers import LevelSerializer, ReportDetailsSerializer, ReportSerializer, SchoolUserSerializer, StudentSerializer, SchoolSerializer, TeacherSerializer, UserSerializer, ClassSerializer, ClassStudentSerializer
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
# SCHOOLL ROUTES
#
#
#
# GET ALL SCHOOLS


@api_view(['GET'])
def getSchools(request, pk):
    schools = School.objects.filter(owner_id=pk)
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)

# ADD NEW SCHOOL


@api_view(['POST'])
def addSchool(request):
    owner = request.data['owner_id']
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        school = serializer.data['id']
        school_user = {
            "school": school,
            "user": owner
        }
        school_user_serializer = SchoolUserSerializer(data=school_user)
        if school_user_serializer.is_valid():
            school_user_serializer.save()
            return Response('school user serializer valid')
        else:
            return Response('school user serializer not valid')

    # return Response(serializer.data)

# DELETE SCHOOL


@api_view(['DELETE'])
def deleteSchool(request, pk):
    school = School.objects.get(id=pk)
    school.delete()

    return Response({"message": "School successfully deleted."})

# UPDATE SCHOOL


@api_view(['PUT'])
def updateSchool(request, pk):
    school = School.objects.get(id=pk)
    serializer = SchoolSerializer(
        instance=school, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

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
# CLASS ROUTES
#
#
#


@api_view(['GET'])
def getClasses(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getClassesBySchoolId(request, pk):
    classes = Class.objects.filter(school_id=pk)
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getClassById(request, pk):
    thisClass = Class.objects.get(id=pk)
    serializer = ClassSerializer(thisClass, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def getClassBySchoolAndDate(request, school_pk, date_pk):
    thisClass = Class.objects.filter(school_id=school_pk).filter(day=date_pk)
    serializer = ClassSerializer(thisClass, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getClassesWithClassLists(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addClass(request):
    serializer = ClassSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteClass(request, pk):
    this_class = Class.objects.get(id=pk)
    this_class.delete()

    return Response({"message": "School successfully deleted."})

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


@api_view(['GET'])
def listStudentsByClass(request, pk):
    students = Student.objects.filter(classstudent__class_id=pk)
    serializer = StudentSerializer(students, many=True)

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
# STUDENT ROUTES
#
#
#
# GET ALL STUDENTS


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

# GET STUDENT BY ID


@api_view(['GET'])
def getStudentById(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)

    return Response(serializer.data)

# GET STUDENTS BY OWNER ID


@api_view(['GET'])
def getStudentsByOwner(request, pk):
    students = Student.objects.filter(school_id__owner_id=pk)
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

# GET STUDENTS BY SCHOOL ID


@api_view(['GET'])
def getStudentsBySchoolId(request, pk):
    students = Student.objects.filter(school_id=pk).order_by('last_name')

    paginator = PageNumberPagination()
    paginated_students = paginator.paginate_queryset(students, request)
    serializer = StudentSerializer(paginated_students, many=True)

    return paginator.get_paginated_response(serializer.data)

# GET STUDENTS BY CLASS ID
# @api_view(['GET'])
# def getStudentsByClassId(request, pk):
#     students = Student.objects.filter()

# CREATE NEW STUDENT


@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE STUDENT


@api_view(['PUT'])
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(
        instance=student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE STUDENT


@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response({"message": "Student successfully deleted."})

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
