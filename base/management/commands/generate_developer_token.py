from django.core.management.base import BaseCommand
from base.models import DevToken 
import secrets

def generate_token(length=40):
    # Calculate the number of bytes needed for the desired length
    num_bytes = (length + 1) // 2  # 2 characters per byte

    # Generate token hex
    token_hex = secrets.token_hex(num_bytes)

    # Truncate or pad the token hex to the desired length
    key = token_hex[:length]

    return key

class Command(BaseCommand):
    help = 'Generates and saves a token for the developer.'

    def handle(self, *args, **options):
        # check if a developer token already exists
        if DevToken.objects.exists():
            self.stdout.write(self.style.SUCCESS("Developer token already exists."))
            self.stdout.write(self.style.SUCCESS(f"Developer token: {DevToken.objects.first().token}"))
        else: 
            developer_token = 'fda3b62cfdbff2aaf6c75481c5886738eb2f0578'
            DevToken.objects.create(token=developer_token, description="Developer Token")
            self.stdout.write(self.style.SUCCESS(f"Developer token: {developer_token}"))        