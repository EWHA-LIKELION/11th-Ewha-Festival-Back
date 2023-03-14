from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nickname', 'is_booth']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname'])
        user.set_password(validated_data['password'])
        user.save()

        return user