from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import decorators, status
from rest_framework.response import Response
from users.models import User
from globals.real_time_activity import SendRealTimeActivity


@decorators.api_view(['POST'])
def LoginView (request) :
    try : 
        email = request.data.get('email',None)
        password = request.data.get('password',None)

        if not email : 
            return Response({'message':"email field can not be empty"},status=status.HTTP_400_BAD_REQUEST)
        
        if not password : 
            return Response({'message':"password field can not be empty"},status=status.HTTP_400_BAD_REQUEST)
        
        try : 
            user = User.objects.get(email=email)

            if not user.is_superuser : 
                return Response({'message':"invalid email"},status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist :
            return Response({'message':"invalid email"},status=status.HTTP_400_BAD_REQUEST)

        if user.check_password(password) is False :
            return Response({'message':"invalid password"},status=status.HTTP_400_BAD_REQUEST)
        
        refresh  = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # logic for send real-time activity
        SendRealTimeActivity(
            content = "Logged in the system",
            from_user = user
        )
        return Response(data,status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            "message" : f'error : {error}'
        },status=status.HTTP_400_BAD_REQUEST)




