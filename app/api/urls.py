from django.urls import path, include
from . import views


urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('generator/', views.TempPasswordGenAPIView.as_view(), name='api-password-generator'),
    path('generator/save/', views.CreateGeneratedPasswdAPIView.as_view(), name='api-password-generator-save'),
    path('storage/', views.PasswordsFromStorageListAPIView.as_view(), name='api-storage-list-creation'),
    path('storage/password/<uuid:pk>/', views.PasswordFromStorageDetailAPIView.as_view(), name='api-storage-delete-update-detail')
]
