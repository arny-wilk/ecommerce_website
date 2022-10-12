from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'email', 'password', 'registration_date')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if KeyError:
            raise f"Wrong Password ! {KeyError}"
        user.set_password(validated_data['password'])
        user.save()
        return user
