from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PasswordGenSerializer, StorageSerializer, SaveGenPasswordInStorageSerializer
from main.models import TempGenPassword
from storage.models import PasswordStorage
from storage.secure import encode_password, key
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwner
# Create your views here.


class TempPasswordGenAPIView(ListAPIView):
    serializer_class = PasswordGenSerializer

    def get_queryset(self):
        return TempGenPassword.objects.filter(user=self.request.user)


class CreateGeneratedPasswdAPIView(CreateAPIView):
    serializer_class = SaveGenPasswordInStorageSerializer

    def get_queryset(self):
        return TempGenPassword.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = SaveGenPasswordInStorageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = self.request.user
            passwd = TempGenPassword.objects.get(user=user)
            new_password = PasswordStorage
            new_password.create_passwd_from_generator(
                user=user,
                key=key,
                site=serializer.validated_data['site'],
                password=encode_password(passwd.password)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordsFromStorageListAPIView(ListCreateAPIView):
    serializer_class = StorageSerializer

    def get_queryset(self):
        return PasswordStorage.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = StorageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_password = PasswordStorage()
            new_password.user = self.request.user
            new_password.key = key
            new_password.password = encode_password(serializer.validated_data['password'])
            new_password.site = serializer.validated_data['site']
            new_password.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordFromStorageDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StorageSerializer
    queryset = PasswordStorage.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = StorageSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=True):
            instance.key = key
            instance.password = encode_password(serializer.validated_data['password'])
            instance.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
