from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.models import CustomUser
from users.forms import RegistrUserForm


class RegistrUserView(CreateView):
    model = CustomUser
    template_name = 'registration/registr_user.html'
    form_class = RegistrUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        send_mail(
            'Успешная регистрация',
            f'ПОЗДРАВЛЯЮ!! Вы успешно зарегистрировались!',
            settings.EMAIL_HOST_USER,
            [form.cleaned_data.get('email'), ],
            fail_silently=False,
        )
        return super().form_valid(form)

class UpdateUserView(UpdateView):
    model = CustomUser
    template_name = 'registration/registr_user.html'
    form_class = RegistrUserForm
    success_url = reverse_lazy('login')

