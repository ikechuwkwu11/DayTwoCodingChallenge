# accounts/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import AccessToken

class AccessTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            raise AuthenticationFailed('Authorization token missing')

        try:
            access_token = AccessToken.objects.get(token=token)
        except AccessToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if access_token.is_expired():
            access_token.delete()
            raise AuthenticationFailed('Token has expired')

        return (access_token.user, None)
