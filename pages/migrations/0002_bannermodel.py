# Generated by Django 4.0.6 on 2022-09-12 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collections', models.CharField(max_length=60, verbose_name='collections')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('is_active', models.BooleanField(blank=True, default=False, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
    ]
