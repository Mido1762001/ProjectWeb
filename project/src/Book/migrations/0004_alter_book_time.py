# Generated by Django 3.2.5 on 2021-07-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_alter_book_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
