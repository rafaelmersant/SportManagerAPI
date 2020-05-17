from .models import User, Document
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'creation_date',
                  'created_user', 'user_hash', 'user_role',
                  'athlete_id')


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'creation_date',
                  'created_user', 'user_hash', 'user_role',
                  'athlete_id', 'password')


class DocSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'description', 'category', 'source', 'doc_url',
                  'doc_filename', 'active', 'creation_date', 'created_user')
