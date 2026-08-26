# Create your views here.

from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.contrib.auth import login

import os

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('library:books_list')

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        send_mail(
            subject=subject,
            message=message,
            from_email=os.getenv('EMAIL_HOST_USER'),
            recipient_list=recipient_list
        )

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)

        return super().form_valid(form)
