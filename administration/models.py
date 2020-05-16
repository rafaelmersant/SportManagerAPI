from django.db import models


class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=150)
    name = models.CharField(max_length=255)
    user_hash = models.CharField(max_length=255, blank=True)
    user_role = models.CharField(max_length=20, blank=True)
    athlete_id = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_user = models.EmailField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'


class Document(models.Model):
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='DOC')
    source = models.CharField(max_length=50)
    url_doc = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_user = models.EmailField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.description}'
