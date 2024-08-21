from django.db import models

# Create your models here.

PRODUCT_TYPE = (
    ('Couch', 'Couch'),
    ('Headboard', 'Headboard'),
    ('Chair', 'Chair'),
    ('Ottoman', 'Ottoman'),
    ('Blanket box', 'Blanket box'),
    ('Lamp shade', 'Lamp shade'),
    ('Curtain', 'Curtain'),
    ('Cushion', 'Cushion'),
    ('Scatter cushion', 'Scatter cushion'),
    ('Roman blind', 'Roman blind'),
)


class Product(models.Model):
    product_type = models.CharField(max_length = 200, null = True, choices=PRODUCT_TYPE)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return str(self.product_type)
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except: 
            url = ''
            
        return url
    
class Testimonial(models.Model):
    first_name = models.CharField(max_length = 200, null = True)
    last_name = models.CharField(max_length = 200, null = True)
    review = models.TextField(max_length = 2000, null = True)
    image = models.ImageField(upload_to='images', default='defaultprofile.png', blank=True, null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except: 
            url = ''
            
        return url
class Subscriber(models.Model):
    email = models.EmailField(max_length=200, null=True)
    
    def __str__(self):
        return self.email
    
class EmailInteractions(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.name + " " + self.subject
    
class LoginId(models.Model):
    user_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user_id
    
class Inventory(models.Model):
    item = models.CharField(max_length=200, null = True, blank= True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.item
    
class Client(models.Model):
    name = models.CharField(max_length=200, null = True, blank= True)
    surname = models.CharField(max_length=200, null = True, blank= True)
    phone = models.CharField(max_length=200, null = True, blank= True)
    email = models.EmailField(max_length=200, null = True, blank= True, default="NoEmail@gmail.com")
    
    def __str__(self):
        return self.name + " " + self.surname
    
class Job(models.Model):
    client = models.ManyToManyField(Client, null=True,blank=True)
    item = models.CharField(max_length=200, null = True, blank= True)
    quantity = models.IntegerField(null = True, blank= True)
    item_pic = models.ImageField(null = True, blank= True)
    fabric = models.ImageField(null = True, blank= True)
    description = models.TextField(max_length=300, null = True, blank= True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.client.name + " " + "--->" + self.item
    
    @property
    def itemURL(self):
        try:
            url = self.item_pic.url
        except:
            url=''
        return url
    
    @property
    def fabricURL(self):
        try:
            url = self.fabric.url
        except:
            url=''
        return url