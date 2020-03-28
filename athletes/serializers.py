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

    document = DocumentSerializer(many=False, read_only=True)

    birthday = serializers.DateField(
        format="%m-%d-%Y", input_formats=['%Y-%m-%d', 'iso-8601'])

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'email',
                  'phone_number', 'photo', 'address', 'birthday',
                  'enrollment_year', 'enrollment_month',
                  'medical_information', 'age', 'creation_date',
                  'created_user', 'parent', 'document')
