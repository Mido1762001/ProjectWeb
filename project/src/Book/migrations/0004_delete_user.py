# Generated by Django 3.2.5 on 2021-07-15 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
