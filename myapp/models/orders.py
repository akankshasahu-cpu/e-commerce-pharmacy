from datetime import datetime
from django.db import models
from .products import Product
from .customer import Customer


class Orders(models.Model):
    products = models.ForeignKey(Product,
                                 on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=12, default='', blank=True)
    date = models.DateField(default=datetime.today)
    completed = models.BooleanField(default=False)
    amount = models.IntegerField(default=1)
    payment = models.BooleanField(default=True)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders \
            .objects \
            .filter(customer=customer_id) \
            .order_by('-date')
