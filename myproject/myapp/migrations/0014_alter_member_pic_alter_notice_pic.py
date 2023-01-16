# Generated by Django 4.1.3 on 2022-12-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_member_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.FileField(default='media/set.png.png', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
