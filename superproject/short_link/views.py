from typing import Any

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from short_link.forms import UserSignupForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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
