from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Geekshop - Панель администратора'}
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def users(request):
    context = {
        'title': 'Geekshop - Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'admins/user_read.html', context)


@user_passes_test(lambda u: u.is_staff)
def user_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'Geekshop - Новый пользователь',
        'form': form,
    }
    return render(request, 'admins/user_create.html', context)


@user_passes_test(lambda u: u.is_staff)
def user_update(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Данные успешно изменены')
            return HttpResponseRedirect(reverse('admins:users'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {
        'title': 'Geekshop - Редактирование пользователя',
        'form': form,
        'user': user,
    }
    return render(request, 'admins/user_update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.save_delete()
    return HttpResponseRedirect(reverse('admins:users'))
