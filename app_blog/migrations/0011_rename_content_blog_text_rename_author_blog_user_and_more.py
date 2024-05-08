# Generated by Django 4.0.1 on 2024-05-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0010_alter_ecologicaltopic_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='sub_title',
        ),
        migrations.AlterField(
            model_name='blog',
            name='topics',
            field=models.ManyToManyField(related_name='blogs', to='app_blog.EcologicalTopic', verbose_name='экологические темы'),
        ),
    ]
