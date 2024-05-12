from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name
    

# Create your models here.
class Products(models.Model):
    PHONE = 'phone'
    APLIANCES = 'apliances'
    LAPTOP = 'laptop'

    TAG = (
        ('phone', PHONE),
        ('apliances', APLIANCES),
        ('laptop', LAPTOP)
    )
    title = models.CharField(max_length=100)
    img = models.ImageField()
    price = models.CharField(max_length=50)
    description = models.TextField()
    type = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tag = models.CharField(max_length=50, choices=TAG)

    @property
    def imageURL(self):
        return self.img.url
    
