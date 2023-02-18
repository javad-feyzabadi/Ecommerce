import random

from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages

from utils import send_otp_code

from . forms import UserRegistrationForm,VerifyCodeForm
from . models import OtpCode

class UserRegistrations(View):
    form_class = UserRegistrationForm    

    def get(self,request):
        form = self.form_class
        return render(request,'accounts/register.html',{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone'],random_code)
            OtpCode.objects.create(phone_number =form.cleaned_data['phone'],code = form.cleaned_data['code'])
            request.sesssion['user_registration_info'] = {
                'phone_number':form.cleaned_data['phone'],
                'email':form.cleaned_data['email'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password'],

            }
            messages.success(request,'We Sent You A Code','success')
            return redirect('accounts:verify_code')
        return redirect('home:home')



class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    def get(self,request):
        pass
    
    def post(self,request):
        pass