# Generated by Django 4.1.3 on 2023-01-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_nil_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nil',
            name='pic',
            field=models.FileField(blank=True, default='set.png.png', null=True, upload_to='media/'),
        ),
    ]
