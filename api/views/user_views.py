from api.serializers import SchoolUserSerializer, TeacherSerializer, UserSerializer
from schools.models import SchoolUser
from users.models import Teacher, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

# ADD NEW USER


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# PARTIAL UPDATE USER

@api_view(['PATCH'])
def updateUser(request, user_pk):
    try:
        user = User.objects.get(id=user_pk)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ADD NEW TEACHER

@api_view(['POST'])
def addTeacher(request):
    try:
        # check if the user exists at all
        user = User.objects.get(email=request.data['email'])
        school_user = {
            "school": request.data['school'],
            "user": user.id
        }
        serializer = SchoolUserSerializer(data=school_user)
        if serializer.is_valid():
            serializer.save()
        
        user_data = {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }

        teacher_serializer = TeacherSerializer(data=user_data, many=False)
        
        if teacher_serializer.is_valid():
            print('ok')

        return Response(teacher_serializer.data)

    except User.DoesNotExist:
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            school_user = {
                "school": request.data['school'],
                "user": serializer.data['id']
            }
            school_user_serializer = SchoolUserSerializer(data=school_user)
            if school_user_serializer.is_valid():
                school_user_serializer.save()

            return Response(serializer.data)

        
# GET TEACHERS FOR SPECIFIC SCHOOL

@api_view(['GET'])
def getTeachersBySchool(request, school_pk, owner_pk):
    school_users = SchoolUser.objects.filter(school=school_pk).exclude(user=owner_pk)
    
    user_ids = []
    for school_user in school_users:
        user_ids.append(school_user.user)

    users = Teacher.objects.filter(email__in=user_ids)
    serializer = TeacherSerializer(users, many=True)

    return Response(serializer.data)