# Generated by Django 5.0.7 on 2024-11-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_remove_travel_title2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='travel',
            name='month_departure',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
