from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='test22@gmail.com',
            first_name='Admin',
            last_name='AdminBig',

        )

        user.set_password('2717')


        user.is_staff = True
        user.is_superuser = True


        user.save()

        self.stdout.write(self.style.SUCCESS(f'Администратор успешно создан; email: {user.email}'))