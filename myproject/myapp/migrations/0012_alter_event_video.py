# Generated by Django 4.1.3 on 2022-12-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.FileField(blank=True, default='media/video/1(1).mp4', null=True, upload_to='media/video/'),
        ),
    ]