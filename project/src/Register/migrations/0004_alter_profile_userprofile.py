# Generated by Django 3.2.5 on 2021-07-18 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0003_alter_profile_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userprofile',
            field=models.ImageField(upload_to='images/%y/%m/%d'),
        ),
    ]
