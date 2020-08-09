from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True )
    slug = models.SlugField(max_length=250, unique=True )
    description = models.TextField(blank=True)
    image = models.ImageField( upload_to='category', blank=True )

    class Meta():
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True )
    slug = models.SlugField(max_length=250, unique=True )
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    image = models.ImageField( upload_to='product', blank=True )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)