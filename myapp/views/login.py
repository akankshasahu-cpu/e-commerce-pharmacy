from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View
from myapp.models.customer import Customer


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        customer = Customer.get_customer_by_email(email)

        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['Email'] = customer.email

                return redirect("homepage")
            else:
                error_message = 'email or password invalid'

        else:
            error_message = 'email or password invalid'

        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('loginpage')
