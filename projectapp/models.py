from django.db import models
from django.contrib.auth.models import User
class book(models.Model):
    Name=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    price=models.IntegerField()
    Image=models.ImageField(upload_to='images/')
    is_featured=models.BooleanField(default=False)
    is_popular=models.BooleanField(default=False)
    is_offer=models.BooleanField(default=False)
    def __str__(self):
        return self.Name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity