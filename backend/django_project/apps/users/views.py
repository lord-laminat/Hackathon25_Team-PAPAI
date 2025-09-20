from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import RegistrationSerializer, LoginSerializer, CustomUserSerializer


class RegistrationView(APIView):
    """ Registration endpoint """

    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    renderer_classes = (JSONRenderer, )


    def post(self, request):
        """
        POST request
        Args:
            request: headers
        """

        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """ Logining endpoint"""
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    renderer_classes = (JSONRenderer, )


    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomUserRetrieve(APIView):
    """ CustomUser data retreive endpoint """
    permission_classes = (IsAuthenticated, )
    serializer_class = CustomUserSerializer

    renderer_classes = (JSONRenderer, )


    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    pass