from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'creation_date',
                  'created_user', 'user_hash', 'user_role', 'password')
