# Generated by Django 5.0.6 on 2024-05-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0011_rename_rate_review_rate_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.ImageField(upload_to='static/imnages/rooms'),
        ),
    ]
