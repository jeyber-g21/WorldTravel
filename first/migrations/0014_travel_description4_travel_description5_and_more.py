# Generated by Django 5.0.7 on 2024-11-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0013_remove_travel_booking_travel_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='description4',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='description5',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='description6',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='description7',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='description8',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='description9',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='image5',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='image6',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='image7',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='image8',
            field=models.CharField(max_length=900, null=True),
        ),
    ]
