from django.urls import path
from .views import return_password

urlpatterns = [
    path('', return_password, name='home')
]
