# Generated by Django 2.2.4 on 2020-03-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0005_auto_20200328_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='photo_filename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='document_filename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
