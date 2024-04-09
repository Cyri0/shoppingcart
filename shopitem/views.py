from django.shortcuts import render, redirect
from .models import ShopItem, OrderItem, Order
# Create your views here.

def processOrder(request):
    if(request.method == 'POST'):
        print("Frontend üzenete:")
        print(request.POST['message'])
    
    #res = {'message': [{'id': '1', 'name': 'alma (1kg)', 'amount': 3}, {'id': '2', 'name': 'barmi', 'amount': 5}]}

    # o = Order()
    # o.save()
    
    # for o_item in res['message']:
    #     id = o_item['id']
    #     amount = o_item['amount']

    #     item = ShopItem.objects.get(id=id)

    #     orderItem = OrderItem()
    #     orderItem.shopitem = item
    #     orderItem.amount = amount
    #     orderItem.save()

    #     o.items.add(orderItem)
    # o.save()

    return redirect('index')