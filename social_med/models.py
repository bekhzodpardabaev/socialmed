from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='media/news')
    subtitle = models.CharField(max_length=255)
    text = models.TextField()
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title


class Ads(models.Model):
    title = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField()
    subtitle = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title
