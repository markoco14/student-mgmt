"""
holds all school related api views
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from schools.models import School, SchoolDay, SchoolUser
from schools.serializers import *
from users.models import Teacher


# GET ALL SCHOOLS


@api_view(['GET'])
def list_schools(request):
    """
    list all schools
    """
    if not request.user.is_superuser:
        return Response({"detail": "Permission denied."})
    
    schools = School.objects.all()
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


# GET SCHOOL BY SCHOOL ID

@api_view(['GET'])
def get_school_by_slug(request, school_slug):
    """
    get a single school by id
    """
    if not request.user:
        return Response({"detail": "User not found."}, status=status.HTTP_401_UNAUTHORIZED)
    
    schools = School.objects.get(slug=school_slug)
    serializer = SchoolSerializer(schools, many=False)

    return Response(serializer.data)



@api_view(['GET'])
def get_school_by_id(request, school_pk):
    """
    get a single school by id
    """
    if not request.user:
        return Response({"detail": "User not found."}, status=status.HTTP_401_UNAUTHORIZED)
    
    schools = School.objects.get(id=school_pk)
    serializer = SchoolSerializer(schools, many=False)

    return Response(serializer.data)


# ADD NEW SCHOOL
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_school(request):
    """
    create a new school
    """
    if not request.user:
        return Response(
            {"detail": "User not found."},
            status=status.HTTP_401_UNAUTHORIZED
            )
    
    if request.user.membership != "OWNER":
        return Response(
            {"detail": "You don't have permission to create schools. Please change your membership if you want to create your own school."},
            status=status.HTTP_401_UNAUTHORIZED
            )
    
    school_serializer = SchoolSerializer(data={
        "name": request.data["name"],
        "slug": request.data["slug"],
        "owner": request.user.id
        })

    if school_serializer.is_valid():
        school = school_serializer.save()
    else:
        return Response(
            {"detail": "School serializer not valid"},
            status=status.HTTP_400_BAD_REQUEST
            )

    school_user = {
        "school": school.id,
        "user": request.user.id,
        "role": SchoolUser.ROLE_OWNER,
    }

    school_user_serializer = SchoolUserSerializer(data=school_user)

    if school_user_serializer.is_valid():
        school_user_serializer.save()
    else:
        return Response(
            {"detail": "School user serializer not valid"},
            status=status.HTTP_400_BAD_REQUEST
            )
    
    return Response(
        data=school_serializer.data,
        status=status.HTTP_201_CREATED
        )

    # return Response(serializer.data)

# DELETE SCHOOL


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_school(request, school_pk):
    """
    delete a school
    """
    if not request.user:
        return Response({"detail": "User not found."}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        school = School.objects.get(id=school_pk)
    except School.DoesNotExist as e:
        return Response({"detail": "Could not find school to delete."}, status=status.HTTP_404_NOT_FOUND)
    
    if school.owner.id != request.user.id:
        return Response({"detail": "Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)

    school.delete()

    return Response({"message": "School successfully deleted."})

# UPDATE SCHOOL


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_school(request, school_pk):
    """
    update school requiring all data
    """
    if not request.user:
        return Response({"detail": "User not found."}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        school = School.objects.get(id=school_pk)
    except School.DoesNotExist as e:
        return Response({"detaiil": "Coult not find school to update."}, status=status.HTTP_404_NOT_FOUND)
    
    if school.owner.id != request.user.id:
        return Response({"detail": "Permission denied."}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = SchoolSerializer(
        instance=school, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"detail": "School serializer invalid."})

    return Response(serializer.data)


#
#
# SCHOOL USER ACCESS ROUTES
#
#
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_schools(request):
    """
    list schools users can access
    """
    if not request.user:
        return Response({"detail": "User not found."})
    
    schools = School.objects.filter(school_users__user_id=request.user.id).distinct()
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





