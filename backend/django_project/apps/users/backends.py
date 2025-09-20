import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import CustomUser

class JWTAuthentication(authentication.BaseAuthentication):
    """ Backend for JWT authentication logic """

    authentication_header_prefix = 'Token'


    def authenticate(self, request):
        """
        Returns:
            None: - returns if authentication cannot be processed\n
            Tuple: - returns (user, token) if authentication was processed successly
        """

        request.user = None

        auth_header = authentication.get_authorization_header(request).split() # ["Token", JWT]
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1 or len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode()
        token = auth_header[1].decode()

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)


    def _authenticate_credentials(self, request, token):
        """
        Try to authenticate with givet credentials
        Args:
            request: - headers
            token: - jwt
        Returns:
            - (user, token) if success else Exception
        """
        print("auth")
        
        try:
            # payload = jwt.decode(token, settings.SECRET_KEY)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except Exception:
            msg = 'Ошибка аутентификации. Невозможно декодировать токеню'
            print(msg)
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = CustomUser.objects.get(pk=payload['id'])
        except CustomUser.DoesNotExist:
            msg = 'Пользователь соответствующий данному токену не найден.'
            print(msg)
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'Данный пользователь деактивирован.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)