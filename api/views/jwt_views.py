from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from schools.models import SchoolAccessPermission

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        permission_queryset = SchoolAccessPermission.objects.filter(user_id=user.id)
        permissions = []
        for permission in permission_queryset:
            permissions.append(permission.role_id.id)

        # Add custom claims
        token['name'] = user.first_name
        token['role'] = user.role
        token['permissions'] = permissions
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer