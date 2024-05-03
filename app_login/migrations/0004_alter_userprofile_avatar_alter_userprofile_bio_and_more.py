# Generated by Django 4.0.1 on 2024-05-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0003_remove_userprofile_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='avatars', verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(verbose_name='о себе'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=20, verbose_name='местоположение'),
        ),
    ]
