# Generated by Django 4.2.20 on 2025-03-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_horse_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='horse/'),
        ),
    ]
