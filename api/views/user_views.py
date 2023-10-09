"""
holds all user related views
"""

from api.serializers.serializers import AdminSerializer, TeacherSerializer, UserSerializer
from api.serializers.user_serializers import ChangePasswordSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from schools.models import Role
from schools.school_serializers import SchoolAccessPermissionSerializer
from users.models import Teacher, User


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

# GET USER PROFILE BY USER ID


@api_view(['GET'])
def getUserProfileById(request, user_pk):
    try:
        user = User.objects.get(id=user_pk)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(user, many=False)

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

    serializer = UserProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UPDATE PASSWORD


@api_view(['PATCH'])
def changePassword(request, user_pk):
    try:
        user = User.objects.get(id=user_pk)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        if not user.check_password(serializer.validated_data['current_password']):
            return Response({"current_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"detail": "Password updated successfully."})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TEACHER VIEWS

# GET ALL TEACHERS
@api_view(['GET'])
def listTeachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def listSchoolTeachers(request):
    teacher_role = Role.objects.get(name='Teacher')
    school = request.query_params.get('school')
    if school:
        teacher_users = User.objects.filter(access_permissions__role_id=teacher_role, access_permissions__school_id=school)
    else:
        teacher_users = User.objects.filter(access_permissions__role_id=teacher_role)
    serializer = UserSerializer(teacher_users, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def listSchoolAdmins(request):
    admin_role = Role.objects.get(name='Admin')
    school = request.query_params.get('school')
    if school:
        admin_users = User.objects.filter(access_permissions__role_id=admin_role, access_permissions__school_id=school)
    else:
        admin_users = User.objects.filter(access_permissions__role_id=admin_role)
    serializer = UserSerializer(admin_users, many=True)

    return Response(serializer.data)

# ADD NEW TEACHER
@api_view(['POST'])
def addTeacher(request):
    teacher_role = Role.objects.get(name="Teacher")
    school_id = request.data['school']
    try:
        # check if the user exists at all
        user = User.objects.get(email=request.data['email'])

        access_permission = {
            "school_id": school_id,
            "user_id": user.id,
            "role_id": teacher_role.id,
        }
        # print(access_permission)

        permission_serializer = SchoolAccessPermissionSerializer(
            data=access_permission)
        if permission_serializer.is_valid():
            new_permission = permission_serializer.save()

        # return this user
        if new_permission:
            user_serializer = TeacherSerializer(user, many=False)

            return Response(user_serializer.data)

        return Response({"details": "Unable to save user access permissions"})

    except User.DoesNotExist:
        new_teacher_serializer = TeacherSerializer(data=request.data)
        if new_teacher_serializer.is_valid():
            new_teacher_serializer.save()

            access_permission = {
                "school_id": school_id,
                "user_id": new_teacher_serializer.data['id'],
                "role_id": teacher_role.id,
            }

            permission_serializer = SchoolAccessPermissionSerializer(
                data=access_permission)

            if permission_serializer.is_valid():
                permission_serializer.save()

            return Response(new_teacher_serializer.data)
        

# ADD NEW Admin
@api_view(['POST'])
def addAdmin(request):
    admin_role = Role.objects.get(name="Admin")
    school_id = request.data['school']
    try:
        # check if the user exists at all
        user = User.objects.get(email=request.data['email'])

        access_permission = {
            "school_id": school_id,
            "user_id": user.id,
            "role_id": admin_role.id,
        }
        # print(access_permission)

        permission_serializer = SchoolAccessPermissionSerializer(
            data=access_permission)
        if permission_serializer.is_valid():
            new_permission = permission_serializer.save()

        # return this user
        if new_permission:
            user_serializer = AdminSerializer(user, many=False)

            return Response(user_serializer.data)

        return Response({"details": "Unable to save user access permissions"})

    except User.DoesNotExist:
        new_admin_serializer = AdminSerializer(data=request.data)
        if new_admin_serializer.is_valid():
            new_admin_serializer.save()

            access_permission = {
                "school_id": school_id,
                "user_id": new_admin_serializer.data['id'],
                "role_id": admin_role.id,
            }

            permission_serializer = SchoolAccessPermissionSerializer(
                data=access_permission)

            if permission_serializer.is_valid():
                permission_serializer.save()

            return Response(new_admin_serializer.data)
