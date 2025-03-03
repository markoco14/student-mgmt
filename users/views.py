"""
holds all user related views
"""
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserSerializer, ChangePasswordSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from users.models import User


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
def addOwnerMembershipUser(request):
    data = request.data.copy()
    data["membership"] = User.MEMBERSHIP_OWNER
    data["email"] = data["username"]
    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        user = serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    
    return Response(
        {
            "accessToken": str(access_token),
            "refreshToken": str(refresh)
        },
        status=status.HTTP_201_CREATED)

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
