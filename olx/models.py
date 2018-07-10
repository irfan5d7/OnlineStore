from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='product_image/',blank=True)
    price = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    buyer = models.CharField(max_length=32,blank=True)
    posted_on = models.DateField(("Date"),blank=True)
    sold_on = models.DateField(("Date"),blank=True)
    description = models.TextField(max_length=2048,blank=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    product = models.ForeignKey(Product,on_delete= models.CASCADE)

    def __str__(self):
        return "cart"

class Comments(models.Model):
    product = models.ForeignKey(Product,on_delete= models.CASCADE,blank=True)
    comments = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "comments"
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to= 'profile_images/',blank=True)
    contact_no = models.CharField(max_length=13)
    address = models.TextField()
    def __str__(self):
        return self.user.username
