import requests


def get_status(url):

    request = requests.get(url)

    return request.status_code
