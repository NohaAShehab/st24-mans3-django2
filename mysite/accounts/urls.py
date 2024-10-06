
from django.urls import include, path
from accounts.views import  profile, AccountCreatioForm


urlpatterns=[
    path("", include("django.contrib.auth.urls")),
    path("profile/",profile, name='accounts.profile' ),
    path("register", AccountCreatioForm.as_view(), name='accounts.register')
]