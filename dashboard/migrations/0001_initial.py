# Generated by Django 5.0 on 2023-12-18 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('destination', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('tour_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
