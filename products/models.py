from django.db import models
from base.models import BaseModel
from django.utils.text import slugify 
# Create your models here.

# Product Category Model
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")
    
    # generate slug automatically function
    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.category_name

# Product Color Variant Model
class ColorVariant(BaseModel):
    color = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.color
    
# Product Size Variant Modal
class SizeVariant(BaseModel):
    size = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size
    
# Product Model
class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products_category', on_delete=models.CASCADE)
    price = models.IntegerField()
    product_desc = models.TextField(blank=True, null=True)
    product_color = models.ManyToManyField(ColorVariant, blank=True, null=True)
    product_size = models.ManyToManyField(SizeVariant, blank=True, null=True)
    
    # Product slug generate automatically funtion 
    def save(self, *args, **kwargs):
        self.product_slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name
    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="products")
    

