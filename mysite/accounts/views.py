from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.views.generic.edit import CreateView
from accounts.forms import  RegistrationForm
# Create your views here.

# authenticated user info --> request ??

# only authenticated users can access this page ??
@login_required()
def profile(request):
    return render(request, 'accounts/profile.html')


class AccountCreatioForm(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login"


