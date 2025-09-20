from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import RegistrationSerializer, LoginSerializer


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