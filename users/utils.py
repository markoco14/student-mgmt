from users.models import User


def get_current_user(email: str) -> User:
    user = User.objects.filter(email=email).first()
    if not user:
        raise Exception({"detail": "User not found."})
   
    return user
