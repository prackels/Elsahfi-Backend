from rest_framework import decorators, permissions, status
from rest_framework.response import Response
from ..models import User


@decorators.api_view(["PUT"])
@decorators.permission_classes([permissions.IsAdminUser])
def UpdateUserPassword(request,userid) : 
    try : 
        
        try : 
            user = User.objects.get(id=userid)
        except User.DoesNotExist:
            return Response({
                'message' : 'user not found'
            },status=status.HTTP_404_NOT_FOUND)
        
        password = request.data.get('password',None)

        if not password or password is None : 
            return Response({
                'message' : "please enter the password"
            },status=status.HTTP_400_BAD_REQUEST)


        user.set_password(password)
        user.save()

        return Response({
            'message' : 'password updated successfully!'
        },status=status.HTTP_200_OK)
     
    except Exception as error :
        return Response({
            'message':f"an error accured : {error}"
        },status=status.HTTP_400_BAD_REQUEST)