from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from django.core.cache import cache
from users.models import User
from random import randrange
from django.template.loader import render_to_string 
from core.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from datetime import timedelta


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def rest_password_view (request) : 
    try : 
        email = request.data.get('email',None)
        current_user = request.user

        if email is None : 
            return Response({
                'message' : "email field cannot be empty"
            },status=status.HTTP_400_BAD_REQUEST)

        try : 
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                'message' : 'this email not found in the system'
            },status=status.HTTP_400_BAD_REQUEST)
        
        if email != current_user.email : 
            return Response({
                'message' : 'this is not your email'
            },status=status.HTTP_400_BAD_REQUEST)
        
        generated_otp = ''.join(map(str,[randrange(0,9) for i in range(6)]))
        cache.set(f'user-otp-{user.id}',generated_otp,timeout=timedelta(hours=2).total_seconds())


        html_template = 'reset_password.html'
        html_message = render_to_string(html_template, { 'otp': generated_otp,'full_name' : user.full_name })

        subject = "Reset Password"
        message = EmailMessage(subject, html_message, EMAIL_HOST_USER, [email])
        message.content_subtype = 'html' 
        message.send()


        return Response({
            'message' : f"otp sent successfully to {email}"
        },status=status.HTTP_200_OK)


    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)