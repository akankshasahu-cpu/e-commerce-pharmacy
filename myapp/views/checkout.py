from django.shortcuts import render, redirect
from django.views import View
from myapp.models import Orders, Customer
from myapp.models.products import Product
from myapp.templatetags.cart import total_cart_price


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        product = Product.get_products_by_id(list(request.session.get('cart').keys()))
        amount = request.POST.get('amount')
        print(address, phone, customer, cart, product)
        for products in product:
            print(cart.get(str(products.id)))
            order = Orders(customer=Customer(id=customer),
                           products=products,
                           price=products.price,
                           address=address,
                           phone=phone,
                           quantity=cart.get(str(products.id)),
                           amount=amount
                           )

            order.placeOrder()
            request.session['cart'] ={}
        return redirect('cartpage')
