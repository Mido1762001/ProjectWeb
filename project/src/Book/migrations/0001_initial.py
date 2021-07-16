# Generated by Django 3.2.5 on 2021-07-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='photoes/%y/%m/%d')),
                ('time', models.TimeField()),
                ('author', models.CharField(max_length=150)),
                ('pages', models.CharField(max_length=10)),
                ('name_Book', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]