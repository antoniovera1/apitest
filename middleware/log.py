import time
import os
from datetime import datetime

from django.conf import settings


class ResponseTimeLogMiddleware:
    """
    Middleware used to log the duration from the moment the API is called
    until the response is sent.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
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