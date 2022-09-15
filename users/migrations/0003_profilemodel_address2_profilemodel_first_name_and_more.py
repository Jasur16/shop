# Generated by Django 4.0.6 on 2022-09-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]