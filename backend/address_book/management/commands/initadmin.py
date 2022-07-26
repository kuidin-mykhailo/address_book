from django.core.management.base import BaseCommand
import django.contrib.auth


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = django.contrib.auth.get_user_model()
        user = User.objects.create_user('admin', password='admin')
        user.is_superuser = True
        user.is_staff = False
        user.save()
