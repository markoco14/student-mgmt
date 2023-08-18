from rest_framework.response import Response
from rest_framework.decorators import api_view
from schools.models import School, SchoolUser
from users.models import Teacher
from ..serializers.serializers import SchoolTeacherSerializer, SchoolUserSerializer, SchoolSerializer, TeacherSerializer

# GET ALL SCHOOLS


@api_view(['GET'])
def listSchools(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


# GET SCHOOL BY SCHOOL ID


@api_view(['GET'])
def getSchoolById(request, school_pk):
    schools = School.objects.get(id=school_pk)
    serializer = SchoolSerializer(schools, many=False)

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
def deleteSchool(request, school_pk):
    school = School.objects.get(id=school_pk)
    school.delete()

    return Response({"message": "School successfully deleted."})

# UPDATE SCHOOL


@api_view(['PUT'])
def updateSchool(request, school_pk):
    school = School.objects.get(id=school_pk)
    serializer = SchoolSerializer(
        instance=school, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#
#
#
# SCHOOL USER ACCESS ROUTES
# THESE ROUTES ANSWER WHO CAN ACCESS THE SCHOOLS
# AND TO WHAT LEVEL CAN THEY ACCESS THE SCHOOLS
#
#
#
@api_view(['GET'])
def listUserSchools(request, user_pk):
    schools = School.objects.filter(school_users__user=user_pk)
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


# SCHOOL-TEACHER ROUTES
@api_view(['GET'])
def getSchoolTeachers(request, school_pk):
    school_users = SchoolUser.objects.filter(school=school_pk)

    user_ids = []
    for school_user in school_users:
        user_ids.append(school_user.user)
    
    teachers = Teacher.objects.filter(email__in=user_ids)
    serializer = SchoolTeacherSerializer(teachers, many=True)

    return Response(serializer.data)




