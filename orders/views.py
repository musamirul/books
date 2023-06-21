from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
