# Generated by Django 4.1.3 on 2022-12-13 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_chairman_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chairman',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
