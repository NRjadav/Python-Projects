# Generated by Django 4.1.3 on 2023-01-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_member_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.FileField(default='media/set.png.png', upload_to='media/images'),
        ),
    ]