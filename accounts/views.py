import jdatetime
from braces.views import (AnonymousRequiredMixin, LoginRequiredMixin,
                          SuperuserRequiredMixin)
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, ListView, View
from ratelimit.decorators import ratelimit

from .models import User
from .forms import LoginForm

user = get_user_model()


# om django.contrib.auth.forms import  Create your views here.

@method_decorator(ratelimit(key='ip', rate='3/m'), name='dispatch')
class AdminLoginView(AnonymousRequiredMixin, View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleand_data
            user_obj = authenticate(phone_number=cd['phone_number'], password=cd['password'])
            if user_obj and user_obj.is_admin:
                login(request, user_obj)
                messages.success(request, 'با موفقیت وارد شدید', 'success')
                return redirect('config:panel')
            messages.error(request, 'خطا در ورود', 'danger')
            return redirect('')
        return render(request, self.template_name, {"form": form})


class AddNewAdminView(SuperuserRequiredMixin, SuccessMessageMixin, CreateView):
    model = user
    form_class =AdminForm
    success_url = reverse_lazy("accounts:admin_list")
    template_name = "accounts/admin_create.html"
    success_message = "ادمین با موققیت اضافه شد"


    def form_valid(self, form):
        new_admin = form.save(commit=False)
        new_admin.is_admin = True
        new_admin.save()
        return super(AddNewAdminView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'خطا در افزودن کاربر ادمین', 'danger')
        return super(AddNewAdminView, self).form_invalid(form)


class UserDeleteView(SuperuserRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        user_obj = get_object_or_404(user, id=user_id)
        user_obj.delete()
        messages.success(request, "", "success")
        return redirect("accounts:admin_list")


class AdminListView(SuperuserRequiredMixin, ListView):
    def get_queryset(self):
        admin_list = user.objects.filter(is_admin=True, is_superuser=False)
        return admin_list

    template_name = 'accounts/admin_list.html'


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, '', 'success')
        return redirect("accounts:login")
