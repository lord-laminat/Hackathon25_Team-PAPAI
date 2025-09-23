from django.urls import path
from .views import RegistrationView, LoginView, CustomUserRetrieve

app_name = 'users'
urlpatterns = [
    path('api/register/', RegistrationView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/retrieve', CustomUserRetrieve.as_view()),
]
