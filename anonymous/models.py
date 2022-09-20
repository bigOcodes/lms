from django.db import models

# Create your models here.
CATEGORY = [
    ('History', ('History')),
    ('Health & body', ('Health & body')),
    ('Religion', ('Religion')),
    ('Computers & Technology', ('Computers & Technology')),
]

class Books(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY)
    author = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Books"


class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name