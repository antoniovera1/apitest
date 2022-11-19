import time
import os
import datetime

from django.conf import settings


class ResponseTimeLogMiddleware:
    """
    Middleware used to log the duration from the moment the API is called
    until the response is sent.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time

        file_name = 'response_time.txt'
        current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        log_entry = (
            f'[{current_datetime}] '
            + f'"{request.method} {request.path} {response.status_code}" '
            + f'Request duration: {duration} secs\n'
        )

        with open(os.path.join(settings.BASE_DIR, file_name), 'a') as fhand:
            fhand.write(log_entry)

        return response