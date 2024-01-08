from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view_order(request):
    orders = Order.objects.all()
    return render(request,"orders/view_order.html",{"orders":orders})


