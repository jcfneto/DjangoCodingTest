from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('email', 'password', 'full_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):

        return get_user_model().objects.create_user(**validated_data)
