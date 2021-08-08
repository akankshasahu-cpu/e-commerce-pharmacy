from django.shortcuts import render
from django.views import View
from myapp.models.products import Product


class Cart(View):

    def get(self, request):
        ids =list(request.session.get('cart').keys())
        product = Product.get_products_by_id(ids)
        print(product)
        return render(request, 'cart.html', {'product': product})
