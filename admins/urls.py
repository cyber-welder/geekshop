from django.urls import path

from admins.views import AdminTemplateView, UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'baskets'

urlpatterns = [
    path('', AdminTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='users'),
    path('user-create/', UserCreateView.as_view(), name='user_create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
