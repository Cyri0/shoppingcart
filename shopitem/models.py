from django.db import models

class ShopItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    shopitem = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.shopitem.name} - {self.amount}db "

class Order(models.Model):
    # TODO User!
    items = models.ManyToManyField(OrderItem)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.date)