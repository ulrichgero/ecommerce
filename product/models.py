from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from djmoney.models.fields import MoneyField
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    tag = models.CharField("add tags - separated by comma", max_length=60)
    is_active = models.BooleanField(default=True)
    cat_image = models.ImageField("add Category Cover here", upload_to='product/category-cover', blank=True)


    class Meta:
        verbose_name = 'Cateogry'
        verbose_name_plural = 'Categories'
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True )
    image = models.ImageField(help_text="add product image", default="default.png", upload_to='product/img/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=60)
    tag = models.ForeignKey(Tag, help_text="add tags - separated by comma", max_length=60, on_delete=models.CASCADE, null=True)
    short_desc = models.CharField(max_length=100)
    full_desc = HTMLField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    avaliable = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

