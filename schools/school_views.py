"""
holds all school related api views
"""

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from schools.school_serializers import *
# SchoolAccessPermissionSerializer,
# SchoolDayListSerializer,
# SchoolDaySerializer,
# SchoolSerializer,
# SchoolTeacherSerializer
from schools.models import School, SchoolDay, SchoolUser
from users import utils as user_utils
from users.models import Teacher, User
from rest_framework import status
from rest_framework.exceptions import NotFound


# GET ALL SCHOOLS


@api_view(['GET'])
def list_schools(request):
    """
    list all schools
    """
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


# GET SCHOOL BY SCHOOL ID


@api_view(['GET'])
def get_school_by_id(request, school_pk):
    """
    get a single school by id
    """
    schools = School.objects.get(id=school_pk)
    serializer = SchoolSerializer(schools, many=False)

    return Response(serializer.data)


# ADD NEW SCHOOL


@api_view(['POST'])
def add_school(request):
    """
    create a new school
    """
    owner = request.data['owner_id']
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        school = serializer.data['id']
        school_user = {
            "school_id": school,
            "user_id": owner,
            "role_id": 1,
        }
        
        school_owner_access_serializer = SchoolAccessPermissionSerializer(data=school_user)
        if school_owner_access_serializer.is_valid():
            school_owner_access_serializer.save()
        else:
            return Response('school user serializer not valid')
    
    return Response(serializer.data)

    # return Response(serializer.data)

# DELETE SCHOOL


@api_view(['DELETE'])
def delete_school(request, school_pk):
    """
    delete a school
    """
    school = School.objects.get(id=school_pk)
    school.delete()

    return Response({"message": "School successfully deleted."})

# UPDATE SCHOOL


@api_view(['PUT'])
def update_school(request, school_pk):
    """
    update school requiring all data
    """
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
def list_user_schools(request):
    """
    list schools users can access
    """
    user = user_utils.get_current_user(email=request.user)
    # user = User.objects.filter(email=request.user).first()
    # if not user:
    #     raise Exception({"detail": "User not found"})
    # print(user)
    schools = School.objects.filter(access_permissions__user_id=user.id).distinct()
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


# SCHOOL-TEACHER ROUTES
@api_view(['GET'])
def get_school_teachers(request, school_pk):
    """
    get users with 'teacher' role at current school
    """
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
    def get(self, request):
        school = request.query_params.get('school', None)
        if school:
            school_days = SchoolDay.objects.filter(school__id=school).order_by('day__id')
            serializer = SchoolDayListSerializer(school_days, many=True)
            return Response(serializer.data)

        school_days = SchoolDay.objects.all()
        serializer = SchoolDayListSerializer(school_days, many=True)
        return Response(serializer.data)

    # Create a new entry
    def post(self, request):
        school_day = {
            'school': request.data['school'],
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





