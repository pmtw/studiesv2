from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'auth/form.html'


class UserLoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'auth/form.html'