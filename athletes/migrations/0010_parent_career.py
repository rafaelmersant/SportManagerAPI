# Generated by Django 2.2.4 on 2020-05-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0009_auto_20200516_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='career',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]