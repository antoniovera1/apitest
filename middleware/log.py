import time
import os
from datetime import datetime

from django.conf import settings


class ResponseTimeLogMiddleware:
    """
    Middleware used to log the duration from the moment the API is called
    until the response is sent.

    Attributes:
        get_response (function): The function to be used to get the response.
            This follows Django convention on middleware implementation as
            explained here:
            https://docs.djangoproject.com/en/4.1/topics/http/middleware/
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        This magic method is called when request comes through the middleware.
        For more information please visit:
            https://docs.djangoproject.com/en/4.1/topics/http/middleware/

        Args:
            request (WSGIRequest): The request which has come to the
                middleware.

        Returns:
            Response: The response from the Django service.
        """

        # Get the time the request was recieved
        start_time = time.time()

        # Get the response
        response = self.get_response(request)

        # Calculate duration
        duration = time.time() - start_time

        # Declare the name of the file where the log will be saved
        file_path = os.path.join(settings.BASE_DIR, 'response_time_log.txt')
        # Get the current time for the log entry
        current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        log_entry = (
            f'[{current_datetime}] '
            + f'"{request.method} {request.path} {response.status_code}" '
            + f'Request duration: {duration} secs\n'
        )

        # Save the log entry on the file
        with open(file_path, 'a') as fhand:
            fhand.write(log_entry)

        return response