from django.urls import path,re_path
from .views import createAccount, Login,updateUser
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    re_path("signup/",createAccount.as_view()),
    re_path("login/",Login.as_view()),
     re_path("updatepassword",updateUser.as_view()),
]
