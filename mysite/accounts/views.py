from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
# Create your views here.

# authenticated user info --> request ??

# only authenticated users can access this page ??
@login_required()
def profile(request):
    return render(request, 'accounts/profile.html')