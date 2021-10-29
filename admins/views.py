from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


class AdminTemplateView(TemplateView):
    template_name = 'admins/index.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop - Панель администратора'
        return context


class UserListView(ListView):
    model = User
    template_name = 'admins/user_read.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Пользователи'
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:users')
    template_name = 'admins/user_create.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Новый пользователь'
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:users')
    template_name = 'admins/user_update-delete.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админ-панель - Редактирование пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/user_update-delete.html'
    success_url = reverse_lazy('admins:users')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.save_delete()
        return HttpResponseRedirect(success_url)
