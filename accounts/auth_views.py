from django.shortcuts import render, HttpResponse, redirect

from accounts.models import UserAccount
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from accounts.models import UserAccount
from .forms import UserAccountForm

from .utils import generate_ref_code, send_email
from .emails import send_verification_email, send_change_password_email

def register_page(request):
    domain_name = request.build_absolute_uri('/')[:-1]

    if request.method == "POST":
        form = UserAccountForm(request.POST)

        if form.is_valid():
            user = form.save()
            send_verification_email(email=user.email, auth_token=user.email_auth_token, domain_name=domain_name)
            messages.success(request, "Registration successful!")
            
            return render(request, "accounts/check_your_email.html", {'email': user.email})
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
                    
            return render(request, "accounts/register.html", { 'form': form })
                
    user_form = UserAccountForm()

    context = {
        'form': user_form,
    }

    return render(request, "accounts/register.html", context)


def login_page(request):
    # user = request.user
    domain_name = request.build_absolute_uri('/')[:-1]
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if not user.verified_email:
                # Send verification codes again
                send_verification_email(email=user.email, auth_token=user.email_auth_token, domain_name=domain_name)
                messages.info(request, f'This Accounts email is not verified')
                return render(request, "accounts/check_your_email.html", {'email': user.email})

            login(request, user)
            return redirect("/admin/")

        else:
            messages.error(request, f'The email or password is incorrect')

    return render(request, "accounts/login.html")


def logout_page(reqeust):
    logout(reqeust)
    return redirect("/")
