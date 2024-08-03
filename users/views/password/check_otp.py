from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from django.core.cache import cache

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def check_otp_view (request) : 
    try : 
        user = request.user
        new_password = request.data.get('password')
        old_password = request.data.get('old_password')
        otp = request.data.get('otp',None)

        if new_password is None:
            return Response({
                'message' : 'password field cannot be empty'
            },status=status.HTTP_400_BAD_REQUEST)
        
        if otp is None:
            return Response({
                'message' : 'otp field cannot be empty'
            },status=status.HTTP_400_BAD_REQUEST)

        get_otp = cache.get(f'user-otp-{user.id}')


        if get_otp == None:
            return Response({
                'message' : "otp expired"
            },status=status.HTTP_400_BAD_REQUEST)

        if int(get_otp) != int(otp) :
            return Response({
                'message' : 'wrong otp'
            },status=status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(old_password):
            return Response({
                "message": "password didn't match"
            }, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        cache.delete(f'user-otp-{user.id}')

        return Response({
            'message' : "password reseted successfully"
        },status=status.HTTP_200_OK)
    
    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)