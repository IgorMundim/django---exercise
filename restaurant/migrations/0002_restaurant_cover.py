# Generated by Django 4.0.4 on 2022-06-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='restaurant/covers/%Y/%m/%d/'),
        ),
    ]
