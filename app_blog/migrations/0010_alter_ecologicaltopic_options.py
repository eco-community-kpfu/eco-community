# Generated by Django 4.0.1 on 2024-05-03 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0009_fill_ecologicaltopic_titles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ecologicaltopic',
            options={'verbose_name': 'экологическая тема', 'verbose_name_plural': 'экологические темы'},
        ),
    ]
