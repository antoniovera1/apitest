import requests

from rest_framework import exceptions


def get_random_int(min_int: int=0,
                   max_int: int=100,
                   url: str='https://www.random.org/integers/',
                   max_attempts: int=10) -> int:
    """
    Get a random number from the random.org API.

    RANDOM.ORG offers true random numbers to anyone on the Internet. The
    randomness comes from atmospheric noise, which for many purposes is better
    than the pseudo-random number algorithms typically used in computer
    programs. Here we use it to generate a random integer.

    Args:
        min_int (int, optional): The lowest posible integer this function will
            return. Defaults to 0.
        max_int (int, optional): The highest posible integer this function will
            return. Defaults to 100.
        url (str, optional): The URL where you can find the random integer
            generator from the random.org API. Defaults to
            'https://www.random.org/integers/'.
        max_attempts (int, optional): The maximum number of attempts to try to
            connect to the API before raising an exception. Defaults to 10.

    Raises:
        exceptions.APIException: When a connection to the random.org API can
            not be established.

    Returns:
        int: A random integer between min_int and max_int.
    """
    params = {
        'num': 1,
        'col': 1,
        'base': 10,
        'rnd': 'new',
        'format': 'plain',
        'min': min_int,
        'max': max_int,
    }

    attempt_num = 1
    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            random_num = response.json()
            return random_num

        if attempt_num >= max_attempts:
            break
        attempt_num += 1

    raise exceptions.APIException(
        "Could not connect to the random.org service")