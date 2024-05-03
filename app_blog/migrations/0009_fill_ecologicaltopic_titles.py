from django.db import migrations


def create_initial_ecological_posts(apps, schema_editor):
    EcologicalTopic = apps.get_model('app_blog', 'EcologicalTopic')
    initial_topics = [
        "Утилизация пластика",
        "Энергия солнца",
        "Биоразнообразие городов",
        "Лесные пожары",
        "Водные ресурсы",
        "Экологичные транспортные средства",
        "Полезные насекомые",
        "Переработка отходов",
        "Городская зелень",
        "Охрана океанов"
    ]
    ecological_posts = [EcologicalTopic(title=topic) for topic in initial_topics]
    EcologicalTopic.objects.bulk_create(ecological_posts)


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0008_ecologicaltopic_blog_topics'),
    ]

    operations = [
        migrations.RunPython(create_initial_ecological_posts),
    ]
