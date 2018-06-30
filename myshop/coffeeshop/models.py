import datetime

from django.db import models
from django.db.models import Sum, F
from django.utils import timezone

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=20, unique=True)
	def __str__(self):
		return self.name

class DrinkType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
    	return self.name

class Size(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Drink(models.Model):
    price = models.DecimalField(max_digits=4, decimal_places=2)
    drink_type = models.ForeignKey(DrinkType, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    class Meta:
        unique_together = ('drink_type', 'size')
    def __str__(self):
        # return self.drink_type.name + "_" + self.size.name
        return repr(dict(id=self.id, drink_type=self.drink_type.name,
            size=self.size.name, price=self.price))

class Order(models.Model):
    quantity = models.IntegerField()
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT)
    ordered_at = models.DateTimeField('order_timestamp')
    def __str__(self):
        return repr(dict(id=self.id, quantity=self.quantity,
            drink=self.drink.drink_type.name))
    @classmethod
    def total_sales(self):
        return Order.objects.aggregate(total=Sum(F('drink__price') * F('quantity'),
            output_field=models.DecimalField(decimal_places=2)))['total']
