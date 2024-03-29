from django.db import models
import datetime


class Athlete(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    photo = models.CharField(max_length=255, null=True, blank=True)
    photo_filename = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    enrollment_year = models.IntegerField(default=0)
    enrollment_month = models.IntegerField(default=0)
    medical_information = models.CharField(
        max_length=255, null=True, blank=True)
    category = models.CharField(max_length=20, default="")
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    edited_date = models.DateTimeField(blank=True, null=True)
    created_user = models.CharField(max_length=50, null=True)
    objects = models.Manager()

    @property
    def age(self):
        try:
            age_ = (datetime.date.today() - self.birthday) / 365
            return age_.days
        except:
            return 0

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Parent(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    career = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_user = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'


class Document(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    document_url = models.CharField(max_length=255)
    document_filename = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_user = models.CharField(max_length=50)
    objects = models.Manager()
