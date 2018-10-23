from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICE = (
    ('Drafted', 'Drafted'),
    ('Published', 'Published'),
    ('Trashed', 'Trashed'),
)

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True, verbose_name='Дата')
    updated_on = models.DateField(auto_now=True)
    keywords = models.TextField(max_length=500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Drafted')
    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True, verbose_name='Дата')

    def __str__(self):
        return self.content
