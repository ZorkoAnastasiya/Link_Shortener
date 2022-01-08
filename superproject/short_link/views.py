from typing import Any

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView, RedirectView

from short_link.forms import UserSignupForm, UserLoginForm, AddLinkForm
from short_link.models import Links, User


class MyRedirectView(RedirectView):
    """
    Redirect short link to source.
    """

    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Links, short_link=self.kwargs.get("short_link"))
        return obj.full_link


class CreateShortLinkView(LoginRequiredMixin, CreateView):
    """
    Creating a short link and saving the data to the database.
    """

    form_class = AddLinkForm
    template_name = "short_link/add_link.html"
    extra_context = {"title": "Add Url"}
    login_url = "short:link"

    @staticmethod
    def create_short_link():
        import random
        import string
        rand_str = string.ascii_letters + string.digits
        short_link = "".join(random.choice(rand_str) for _ in range(8))
        return short_link

    def form_valid(self, form):
        obj = form.save(commit=False)
        short = self.create_short_link()
        while Links.objects.filter(short_link=short).exists():
            short = self.create_short_link()
        obj.short_link = short
        obj.save()
        user = User.objects.get(id=self.request.user.pk)
        user.links.add(obj)
        return super().form_valid(form)

    def form_invalid(self, form):
        url = form.instance.full_link
        if Links.objects.filter(full_link=url).exists():
            obj = Links.objects.get(full_link=url)
            from django.shortcuts import redirect
            return redirect(obj)
        return super().form_invalid(form)


class LinkView(LoginRequiredMixin, DetailView):
    """
    Demonstration of the full link and its short version.
    """

    model = Links
    template_name = "short_link/link.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["host"] = self.request.get_host()
        return context


class UserLinksView(LoginRequiredMixin, ListView):
    """
    Lists all user links.
    """

    model = Links
    template_name = "short_link/all_links.html"
    extra_context = {"title": "My Links"}
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user.pk
        return super().get_queryset().filter(users=user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["host"] = self.request.get_host()
        return context


class UserSignupView(SuccessMessageMixin, FormView):
    """
    User registration.
    """

    form_class = UserSignupForm
    template_name = "short_link/register.html"
    success_url = reverse_lazy("short:home")
    success_message = "Registration completed successfully!"

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.clean_password2(),
        )
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form: Any) -> HttpResponse:
        messages.error(self.request, "Registration error!")
        return self.render_to_response(
            self.get_context_data(form=form, message=messages)
        )


class UserLoginView(LoginView):
    """
    User authorization.
    """

    form_class = UserLoginForm
    template_name = "short_link/login.html"
