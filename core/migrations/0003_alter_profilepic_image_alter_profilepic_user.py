# Generated by Django 5.0 on 2023-12-24 12:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_profilepic_image_profilepic_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='image',
            field=models.ImageField(upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='profilepic',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='picture', to=settings.AUTH_USER_MODEL),
        ),
    ]