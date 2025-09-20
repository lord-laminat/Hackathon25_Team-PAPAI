from django.urls import path
from .views import RegistrationView

app_name = 'users'
urlpatterns = [
    path('register/', RegistrationView.as_view())
]
