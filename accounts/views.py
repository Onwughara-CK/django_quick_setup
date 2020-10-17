from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import SignUpForm

class IndexView(TemplateView):
    template_name = "accounts/index.html"

class SignUpView(FormView):
    template_name = "accounts/authenticate.html"
    form_class = SignUpForm

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")        
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.info(
            self.request, "You signed up successfully."
        )
        return response
