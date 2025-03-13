# Generated by Django 4.2.20 on 2025-03-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='grain_type',
            field=models.CharField(choices=[('WL', 'Weanling'), ('YL', 'Yearling'), ('WK', 'Working'), ('MT', 'Maintenance'), ('SR', 'Senior')], default='WL', max_length=2),
        ),
    ]
