from .models import Athlete, Parent, Document
from rest_framework import serializers


class ParentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Parent
        fields = ('id', 'name', 'phone_number', 'email',
                  'creation_date', 'created_user')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'title', 'image', 'creation_date',
                  'created_user')


class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    parent = ParentSerializer(many=False, read_only=True)
    parent_id = serializers.IntegerField(write_only=True)

    document = DocumentSerializer(many=False, read_only=True)
    document_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'email',
                  'phone_number', 'photo', 'address', 'birthday',
                  'enrollment_year', 'enrollment_month',
                  'medical_information', 'creation_date',
                  'created_user', 'parent', 'parent_id',
                  'document', 'document_id')
