# Generated by Django 4.1.7 on 2023-03-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_accessrecord_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecord',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
