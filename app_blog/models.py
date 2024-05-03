from django.db import models
from django.contrib.auth.models import User


class EcologicalTopic(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "экологическая тема"
        verbose_name_plural = "экологические темы"


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    title = models.CharField(max_length=150, verbose_name='заголовок')
    sub_title = models.CharField(max_length=264, verbose_name='подзаголовок', null=True, blank=True)
    slug = models.SlugField(max_length=264, unique=True)
    content = models.TextField(verbose_name='текст')
    image = models.ImageField(upload_to='blogs', verbose_name='фотография')
    published = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(EcologicalTopic, related_name="blogs")

    class Meta:
        ordering = ['-published', ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(verbose_name='комментарий', default='')
    commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-commented',)

    def __str__(self):
        return self.comment


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')

    def __str__(self):
        return f"{self.user} likes {self.blog}"
