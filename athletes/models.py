from django.db import models
import datetime


class Athlete(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    photo = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    enrollment_year = models.IntegerField()
    enrollment_month = models.IntegerField()
    medical_information = models.CharField(
        max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_user = models.EmailField(null=True, blank=True)
    objects = models.Manager()

    @property
    def age(self):
        age_ = (datetime.date.today() - self.birthday) / 365
        return age_.days

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Parent(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_user = models.EmailField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'


class Document(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_user = models.EmailField(null=True, blank=True)
    objects = models.Manager()
