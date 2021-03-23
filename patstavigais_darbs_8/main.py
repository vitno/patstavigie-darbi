from wsgiref.simple_server import make_server
import random


def index():

    quotes = [
        "quote 1",
        "quote 2",
        "quote 3",
        "quote 4",
        "quote 5",
    ]

    random_quote = random.choice(quotes)
    response_content = random_quote

    return [response_content.encode()]


def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html; charset=utf-8")]

    path = environ["PATH_INFO"]

    response_content = index()

    start_response(status, headers)

    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}")
    server.serve_forever()
