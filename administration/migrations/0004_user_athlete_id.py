# Generated by Django 2.2.4 on 2020-05-15 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20200514_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='athlete_id',
            field=models.IntegerField(default=0),
        ),
    ]
