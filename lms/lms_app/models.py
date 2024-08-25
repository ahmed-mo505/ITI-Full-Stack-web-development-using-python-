from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Book(models.Model):

    state_book = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'sold'),
    ]



    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='images', null=True, blank=True)
    author_image = models.ImageField(upload_to='images', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rent_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rent_period = models.IntegerField(null=True, blank=True)
    total_rent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=50, choices=state_book, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Books'