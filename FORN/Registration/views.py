from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class signup(FormView):
    form_class = UserCreationForm

    success_url = "/Registration/login"

    template_name = "signup.html"

    def form_valid(self, form):
        form.save()
        return super(signup, self).form_valid(form)


class Login(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(Login, self).form_valid(form)


class LogOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
