from rest_framework import serializers

from .models import Booth, Menu, Image, Comment
from account.models import User

class BoothListSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField(many=True, read_only=True)
    is_liked = serializers.BooleanField(default=False)
    
    class Meta:
        model = Booth
        fields = ['id', 'user', 'day', 'college', 'name', 'number', 'thumnail', 'description', 'is_liked', 'created_at', 'updated_at']
        read_only_fields= ('thumnail', )