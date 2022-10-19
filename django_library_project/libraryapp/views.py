from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status

# Create your views here.

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = UserSerializer(data=request.data)
        if reg_serializer.is_valid():
            usermanager = reg_serializer.save()
            if usermanager:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.erros, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['GET', 'POST'])
#def users_list(request):
    #if request.method == 'GET':
        #data = User.objects.all()
#
        #serializer = UserSerializer(data, context={'request': request}, many=True)
#
        #return Response(serializer.data)
#
    #elif request.method == 'POST':
        #serializer = UserSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(status=status.HTTP_201_CREATED)
#
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#@api_view(['PUT', 'DELETE'])
#def users_detail(request, pk):
    #user = User.objects.get(pk=pk)
    #if User.DoesNotExist:
        #raise Response(status=status.HTTP_404_NOT_FOUND)
#
    #if request.method == 'PUT':
        #serializer = UserSerializer(user, data=request.data, context={'request': request})
        #if serializer.is_valid():
            #serializer.save()
            #return Response(status=status.HTTP_204_NO_CONTENT)
#
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
    #elif request.method == 'DELETE':
        #user.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)
