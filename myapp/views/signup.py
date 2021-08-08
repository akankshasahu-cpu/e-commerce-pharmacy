from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from myapp.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('FirstName')
        last_name = postData.get('LastName')
        email = postData.get('Email')
        password = postData.get('Password')
        phone = postData.get('Phone')
        print(first_name, last_name, email, password, phone)

        # validation
        value = {'first_name': first_name,
                 'last_name': last_name,
                 'email': email,
                 'phone': phone,
                 }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            password=password,
                            email=email,
                            phone=phone)
        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:

            customer.password = make_password(customer.password)
            customer.register()

            return redirect('homepage')

        else:

            data = {
                'error': error_message,
                'values': value
            }

        return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 Character"
        elif (not customer.last_name):
            error_message = "Last Name Required !"
        elif len(customer.last_name) < 2:
            error_message = "Last Name must be 2 Character"
        elif (not customer.email):
            error_message = "email Required !"
        elif len(customer.email) < 4:
            error_message = "email must be 8 Character"
        elif (not customer.phone):
            error_message = "Phone Number Required !"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 digit"
        elif customer.isExists():
            error_message = "email Address Already Registered !"

        return error_message
