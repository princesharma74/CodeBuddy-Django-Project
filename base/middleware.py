from django.http import JsonResponse
from .models import DevToken

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is to an API endpoint
        if request.path.startswith('/api/'):
            # Extract the token from the request headers
            token_key = request.headers.get('Authorization')

            if token_key:
                # Extract the token value from the Authorization header
                try:
                    token_key = token_key.split(' ')[1]
                except IndexError:
                    return JsonResponse({'error': 'Invalid Authorization header'}, status=401)

                # Check if the token exists in the DevToken model
                if not DevToken.objects.filter(token=token_key).exists():
                    return JsonResponse({'error': 'Invalid token'}, status=401)
            else:
                return JsonResponse({'error': 'Authorization header is missing'}, status=401)

        response = self.get_response(request)
        return response
