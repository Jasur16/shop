# Generated by Django 4.0.6 on 2022-07-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_brandmodel_colormodel_sizemodel_productmodel_brands_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='real_price',
            field=models.FloatField(default=0, verbose_name='real price'),
        ),
    ]