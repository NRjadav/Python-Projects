# Generated by Django 4.1.3 on 2023-01-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_nil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nil',
            name='pic',
            field=models.FileField(default='set.png.png', upload_to='media/'),
        ),
    ]
