# Generated by Django 4.0.6 on 2022-11-17 21:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0004_alter_predictions_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='predictions',
            unique_together={('user', 'round', 'prediction')},
        ),
    ]
