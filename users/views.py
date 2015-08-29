from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse_lazy

from users.forms import CreateUserForm


class UserCreateView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('posts')
    template_name = 'form.html'

