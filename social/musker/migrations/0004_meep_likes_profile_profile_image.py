# Generated by Django 4.1.7 on 2023-04-26 13:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musker', '0003_meep'),
    ]

    operations = [
        migrations.AddField(
            model_name='meep',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='meep_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]