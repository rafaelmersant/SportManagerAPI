# Generated by Django 2.2.4 on 2020-05-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_user_athlete_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(default='DOC', max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('url_doc', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('created_user', models.EmailField(max_length=254)),
            ],
        ),
    ]