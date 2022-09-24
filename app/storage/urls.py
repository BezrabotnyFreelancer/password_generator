from django.urls import path
from . import views


urlpatterns = [
    path('', views.PasswordList.as_view(), name='storage_list'),
    path('<uuid:pk>/', views.password_detail, name='storage_detail'),
    path('<uuid:pk>/update/', views.PasswordUpdate.as_view(), name='storage_update'),
    path('<uuid:pk>/delete/', views.PasswordDelete.as_view(), name='storage_delete'),
    path('create/', views.CreatePassword.as_view(), name='create_storage')
]
