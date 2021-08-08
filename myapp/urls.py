from django.urls import path
from .views.cart import Cart
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.checkout import CheckOut
from .views.orderss import Orderss
from .middleware.auth import auth_middleware


urlpatterns = [

    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signuppage'),
    path('login', Login.as_view(), name='loginpage'),
    path('logout', logout, name='logoutpage'),
    path('cart', Cart.as_view(), name='cartpage'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(Orderss.as_view()), name='orders')

]
