# Generated by Django 4.0.6 on 2022-11-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
