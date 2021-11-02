from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, UserCreateView, UserUpdateView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('profile/', login_required(UserUpdateView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
