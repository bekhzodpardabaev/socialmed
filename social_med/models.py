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


class MedicalCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)
    medical_category = models.ManyToManyField('MedicalCategory')
    address = models.CharField(max_length=255)
    metro = models.CharField(max_length=50)
    start_time = models.TimeField(default='9:00')
    end_time = models.TimeField(default='17:00')
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    how_it_works = models.CharField(max_length=255, blank=True, null=True)
    service_information = models.CharField(max_length=255, blank=True, null=True)
    required_documents = models.TextField(blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    responsible_person = models.CharField(max_length=255, blank=True, null=True)
    law = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.title


class Apply(models.Model):
    STATUS_CHOICE = (
        ("NEW", "new"),
        ("COMPLETED", "completed"),
        ("REJECTED", "rejected")
    )
    service = models.ForeignKey('Services', on_delete=models.CASCADE, related_name='apply')
    text = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICE)
    date = models.DateField()

    def __str__(self):
        return self.text
