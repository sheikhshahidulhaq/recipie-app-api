"""Serializers for user API View"""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModalSerializer):
    """Serializer for thr tuser object"""

    class Meta:
        modal = get_user_model()
        fields = ['email','password','name']
        extra_kwargs = {'password':{'write_only':True,'min_length':5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)