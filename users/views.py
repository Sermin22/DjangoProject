import secrets
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login
from .models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    # это из видео в ДЗ
    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Добро пожаловать в наш сервис',
            message = (f'Спасибо, что зарегистрировались в нашем сервисе! '
                       f'Перейдите по ссылке для подтверждения почты и завершения регистрации {url}'),
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


    # это ранее из урока было с Алексеем
    # def form_valid(self, form):
    #     user = form.save()
    #     # login(self.request, user)  # автоматически залогинит пользователя после его регистрации
    #     self.send_welcome_email(user.email)
    #     return super().form_valid(form)
    #
    # def send_welcome_email(self, user_email):
    #     subject = 'Добро пожаловать в наш сервис'
    #     message = 'Спасибо, что зарегистрировались в нашем сервисе!'
    #     from_email = settings.EMAIL_HOST_USER
    #     recipient_list = [user_email]
    #     send_mail(subject, message, from_email, recipient_list)
