from django.urls import path
from .views.login import LoginView
from .views.update_password import UpdateUserPassword
from .views.create import CreateUser
from .views.password.reset_password import rest_password_view
from .views.password.check_otp import check_otp_view
from .views.get import get_all_users, get_user_info
from .views.delete import delete_user
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('login/', LoginView),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('user/update/password/<int:userid>/',UpdateUserPassword),
    path('user/create/',CreateUser),
    path('user/get-all/',get_all_users),
    path('user/info/',get_user_info),
    path('user/delete/<str:email>/', delete_user),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/',rest_password_view),
    path('reset-password/otp/',check_otp_view),
]