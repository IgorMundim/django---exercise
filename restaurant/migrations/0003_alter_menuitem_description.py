# Generated by Django 4.0.4 on 2022-06-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
