from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Группа')
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text

    text = models.TextField(verbose_name='Пост', max_length=255)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to='posts/', blank=True, null=True)


class Comment(models.Model):
    def __str__(self):
        return self.text

    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    text = models.TextField(verbose_name='Комментарий', max_length=255)
    created = models.DateTimeField('date published', auto_now_add=True)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        UniqueConstraint(name='unique_following', fields=['user', 'author'])