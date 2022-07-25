from django.core.management.base import BaseCommand
import django.contrib.auth


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = django.contrib.auth.get_user_model()
        if not User.objects.all().filter(username='admin'):
            user = User.objects.create('admin', password='admin')
            user.is_superuser = True
            user.is_staff = False
            user.save()

