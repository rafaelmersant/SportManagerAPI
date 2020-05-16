from .models import Athlete, Parent, Document
from rest_framework import serializers


class AthleteSerializerFull(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'email',
                  'enrollment_year', 'enrollment_month',
                  'category', 'creation_date',
                  )


class AthleteSerializer(serializers.HyperlinkedModelSerializer):

    # birthday = serializers.DateField(
    #     format="%Y-%m-%d", input_formats=['%Y-%m-%d', 'iso-8601'])

    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'email',
                  'phone_number', 'photo', 'photo_filename', 'address',
                  'birthday', 'enrollment_year', 'enrollment_month',
                  'medical_information', 'age', 'category', 'creation_date',
                  'created_user')


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    athlete = AthleteSerializer(many=False, read_only=True)
    athlete_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Parent
        fields = ('id', 'name', 'phone_number', 'email',
                  'creation_date', 'created_user',
                  'athlete', 'athlete_id')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    athlete = AthleteSerializer(many=False, read_only=True)
    athlete_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Document
        fields = ('id', 'title', 'document_url', 'document_filename',
                  'creation_date', 'created_user', 'athlete', 'athlete_id')
