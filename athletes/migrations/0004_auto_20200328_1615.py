# Generated by Django 2.2.4 on 2020-03-28 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_auto_20200322_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='athlete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='athletes.Athlete'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='athlete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='athletes.Athlete'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]