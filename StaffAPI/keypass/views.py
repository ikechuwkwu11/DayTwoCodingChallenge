from rest_framework.permissions import IsAuthenticated

from .serializer import RegisterSerializer,LoginSerializer,AccessTokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import User,AccessToken
from.authentication import AccessTokenAuthentication
# Create your views here.

class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully registered'},status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class Login(APIView):
    def post(self,request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.filter(username=username).first()
            if user and user.password == password:
                token = AccessToken.objects.create(user=user)
                return Response({'token': token.token,'message':'Login successful'}, status=200)
            return Response({'message':'invalid entering'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)}, status=500)

class Logout(APIView):
    authentication_classes = [AccessTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            AccessToken.objects.filter(user=request.user.delete()).first()
            return Response({'message':'You have been logged out and token invalid'},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class Protected(APIView):
    authentication_classes = [AccessTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            return Response({'message':f'Welcome,{request.user.username}!, you have access'},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)
