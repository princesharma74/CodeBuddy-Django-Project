from django.core.management.base import BaseCommand
from base.models import DevToken 
import secrets

def generate_token(length=40):
    """
    Generate a random token of the specified length.

    Parameters:
    length (int): Length of the token (default is 40)

    Returns:
    str: Random token
    """
    return secrets.token_hex(length)

class Command(BaseCommand):
    help = 'Generates and saves a token for the developer.'

    def handle(self, *args, **options):
        # check if a developer token already exists
        if DevToken.objects.exists():
            self.stdout.write(self.style.SUCCESS("Developer token already exists."))
            self.stdout.write(self.style.SUCCESS(f"Developer token: {DevToken.objects.first().token}"))
        else: 
            developer_token = generate_token()
            DevToken.objects.create(token=developer_token, description="Developer Token")
            self.stdout.write(self.style.SUCCESS(f"Developer token: {developer_token}"))        