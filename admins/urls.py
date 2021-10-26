from django.urls import path

from admins.views import index, users, user_create, user_update, user_delete

app_name = 'baskets'

urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users'),
    path('user-create/', user_create, name='user_create'),
    path('user-update/<int:id>/', user_update, name='user_update'),
    path('user-delete/<int:id>/', user_delete, name='user_delete'),
]
