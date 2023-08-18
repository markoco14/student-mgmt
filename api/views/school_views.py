from rest_framework.response import Response
from rest_framework.decorators import api_view
from schools.models import School, SchoolUser
from users.models import Teacher
from ..serializers.serializers import SchoolTeacherSerializer, SchoolUserSerializer, SchoolSerializer, TeacherSerializer

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
# THESE ROUTES ANSWER WHO CAN ACCESS THE SCHOOLS
# AND TO WHAT LEVEL CAN THEY ACCESS THE SCHOOLS
#
#
#
@api_view(['GET'])
def getSchoolsByUserAccess(request, pk):
    schools = School.objects.filter(school_users__user=pk)
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




