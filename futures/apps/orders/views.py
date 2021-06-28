from django.shortcuts import render
from django.views import View

from .models import (
    Order
)

class OrdersView(View):

    def get(self, request, *args, **kwargs):
        

        orders = Order.objects.all()

        context = {
            "orders": orders
        }

        return render(request, "orders/orders.html", conntext)