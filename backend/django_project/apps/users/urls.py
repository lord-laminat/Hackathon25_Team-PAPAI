from django.urls import path
from .views import RegistrationView, LoginView

app_name = 'users'
urlpatterns = [
    path('api/register/', RegistrationView.as_view()),
    path('api/login/', LoginView.as_view()),
]
