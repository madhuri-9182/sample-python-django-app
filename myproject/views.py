from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def home(request):
    logger.info("Home page visited.")
    return JsonResponse({'message': 'Hello from Django App'})

