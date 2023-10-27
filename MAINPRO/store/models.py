from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)


    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self) :
        return self.title
    


class Product(models.Model)    :
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'Wating approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    )

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_image')
    image1 = models.ImageField( default='')
    image2 = models.ImageField( default='')
    image3 = models.ImageField( default='')
    image4 = models.ImageField( default='')
    thumbnail = models.ImageField(upload_to='uploads/product_images/thumbnail',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self) :
        return self.title
    

    def get_display_price(self):
        return self.price 
    

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https//via.placeholder.com/240x240x.jpg'

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        name = image.name.replace('uploads/product_image/', '')
        thumbnail = File(thumb_io, name=name)

        return thumbnail
    


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid_amount = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=255,blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def get_display_price(self):
        return self.price 
    

    # def subtotal(self):
    #     subtotal = self.price * self.quantity
    #     return sum(subtotal)