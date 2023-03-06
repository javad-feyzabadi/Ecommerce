from datetime import datetime,timedelta

from django.core.management.base import BaseCommand

from accounts.models import OtpCode


class Command(BaseCommand):
    help = 'remove all expired otp codes'
    
    def handle(self, *args, **options):
        expire_time = datetime.now() - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt = expire_time).delete()
        self.stdout.write('all expire otp codes removed.')
