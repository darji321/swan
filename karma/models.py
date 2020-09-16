from django.db import models
from django.contrib.auth.models import User

class Addresses(models.Model):
	address = models.TextField(null=True)
	city = models.CharField(max_length=100,null=True)
	state = models.CharField(max_length=100,null=True)
	zipcode = models.IntegerField(null=True)
	country = models.CharField(max_length=100,null=True)
	
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12,null=True)
    alternate_mobile_number = models.CharField(max_length=12,null=True)
    addresses=models.ManyToManyField(Addresses)

class Products(models.Model):
	img = models.ImageField(upload_to='latest_products')
	desc = models.TextField()
	price = models.IntegerField()
	cancle_price = models.IntegerField()
	qty = models.IntegerField(null=True)
		
class Coming_Products(models.Model):
	img = models.ImageField(upload_to='coming_products')
	desc = models.TextField()
	price = models.IntegerField()
	cancle_price = models.IntegerField()

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	Productid = models.IntegerField(null=True)
	img = models.ImageField()
	desc = models.TextField()
	price = models.IntegerField()
	qty = models.IntegerField(null=True)
	subtotal = models.IntegerField(null=True)
	stock = models.IntegerField(null=True)



