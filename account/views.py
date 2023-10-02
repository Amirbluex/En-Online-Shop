from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm, RegisterForm, CheckOtpForm, UserInformationCreationForm
from django.contrib.auth import login, authenticate, logout
import ghasedakpack
from random import randint
from .models import Otp, User
from uuid import uuid4


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/Login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error('username', 'invalid phone or email')
        else:
            form.add_error('username', 'invalid password')
        return render(request, "account/Login.html", {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "account/Register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(10000, 99999)
            SMS = ghasedakpack.Ghasedak("")
            SMS.verification({'receptor': cd["phone"], 'type': '1', 'template': 'randcode', 'param1': randcode,
                              'param2': 'Multi-shop'})
            token = str(uuid4())
            Otp.objects.create(phone=cd["phone"], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid phone number')

        return render(request, "account/Register.html", {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, "account/Check_otp.html", {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_create = User.objects.get_or_create(phone_number=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect("/")

        else:
            form.add_error('code', 'invalid code')

        return render(request, "account/Check_otp.html", {'form': form})


class AddInformation(View):
    def post(self, request):
        form = UserInformationCreationForm(request.POST)
        if form.is_valid():
            information = form.save(commit=False)
            information.user = request.user
            information.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)

        return render(request, 'account/Add_information.html', {'form': form})

    def get(self, request):
        form = UserInformationCreationForm()
        return render(request, 'account/Add_information.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("/")

