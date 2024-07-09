from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the custom error handling for IntegrityError
    if isinstance(exc, IntegrityError):
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # If an unexpected error is caught, return it as a JSON response
    if response is None:
        return Response({'error': str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
