# Generated by Django 3.2 on 2021-04-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='psize',
            field=models.CharField(default='S', max_length=20),
        ),
    ]
