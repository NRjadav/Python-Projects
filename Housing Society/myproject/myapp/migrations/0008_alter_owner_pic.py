# Generated by Django 4.1.3 on 2023-01-17 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_owner_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='pic',
            field=models.FileField(default='media/images/set.png.png', upload_to='media/images/'),
        ),
    ]
