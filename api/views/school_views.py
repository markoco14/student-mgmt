from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.serializers.school_serializers import SchoolDayListSerializer, SchoolDaySerializer
from schools.models import School, SchoolDay, SchoolUser
from users.models import Teacher
from ..serializers.serializers import SchoolTeacherSerializer, SchoolUserSerializer, SchoolSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound


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

# 
# 
# SCHOOL DAY ROUTES
# 
# 

class SchoolDayList(APIView):
    def get(self, request, school_pk=None):
        if school_pk:
            school_days = SchoolDay.objects.filter(school__id=school_pk).order_by('day__id')
            serializer = SchoolDayListSerializer(school_days, many=True)
            return Response(serializer.data)

        school_days = SchoolDay.objects.all()
        serializer = SchoolDayListSerializer(school_days, many=True)
        return Response(serializer.data)

    # Create a new entry
    def post(self, request, school_pk):
        school_day = {
            'school': school_pk,
            'day': request.data['day']
        }
        # SERIALIZER AND SAVE WITH DAY AS ID VALUE
        serializer = SchoolDaySerializer(data=school_day)
        if serializer.is_valid():
            saved_school_day = serializer.save()
            # RETURN RESPONSE WITH DAY AS STRING VALUE
            response_serializer = SchoolDayListSerializer(saved_school_day, many=False)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SchoolDayDetail(APIView):

    # Utility method to get an object or return a 404 response
    def get_object(self, school_day_pk):
        try:
            return SchoolDay.objects.get(id=school_day_pk)
        except SchoolDay.DoesNotExist:
            raise NotFound(detail="Object with this ID not found.")

    # Retrieve a specific entry by primary key
    def get(self, request, school_day_pk):
        school_day = self.get_object(school_day_pk)
        serializer = SchoolDaySerializer(school_day)
        return Response(serializer.data)

    # Update a specific entry by primary key
    def put(self, request, school_day_pk):
        school_day = self.get_object(school_day_pk)
        serializer = SchoolDaySerializer(school_day, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update a specific entry by primary key
    def patch(self, request, school_day_pk):
        school_day = self.get_object(school_day_pk)
        serializer = SchoolDaySerializer(school_day, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific entry by primary key
    def delete(self, request, school_day_pk):
        school_day = self.get_object(school_day_pk)
        school_day.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





