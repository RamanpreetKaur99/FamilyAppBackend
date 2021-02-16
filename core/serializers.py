
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,Serializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Family, MyUser
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=50)
    family = serializers.IntegerField()

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password', 'name','family')


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'family': self.validated_data.get('family', None),
        }

    def save(self, request):
        user = super().save(request)
        user.name = self.validated_data.get('name')
        family = self.validated_data.get('family')
        print(family)
        if family:
            user.family = Family.objects.get(id = int(family))
        user.save()
        return user


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model=Family
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'