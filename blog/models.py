from django.db import models
 
class Category(models.Model):
    name = models.CharField(max_length=20)

class Carinfo(models.Model):
    year = models.CharField(max_length=10,default='',null=False)
    make = models.CharField(max_length=20,default='',null=False)
    model = models.CharField(max_length=20,default='',null=False)
    price = models.CharField(max_length=20,default='',null=False)
    info = models.CharField(max_length=400,default='',null=False)

 
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
# Create your models here.
