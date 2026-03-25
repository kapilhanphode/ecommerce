from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import UserRateThrottle
from apps.accounts.serializers.auth_serializer import RegisterSerializer, LoginSerializer


class LoginThrottle(UserRateThrottle):
    rate = '5/min'


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User created"}, status=201)


class LoginView(APIView):
    throttle_classes = [LoginThrottle]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        })


class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.data['refresh']
        token = RefreshToken(refresh_token)
        return Response({
            "access": str(token.access_token),
        })
