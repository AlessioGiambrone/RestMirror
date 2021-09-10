from flask import Flask, request
from json import dumps
from os import environ
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    '''There isn't a "real" endpoint to this app, while all we want to do
    is to reply with the request's data.
    '''
    data = request.get_data().decode('UTF8')
    args = dumps(request.args)
    files = request.files
    if not data:
        data = None
    headers = {k[0]: k[1] for k in request.headers}

    app_response = {
        'method': request.method,
        'headers': headers,
        'data': data,
        'args': args,
        'files': files
        }
    print(app_response)

    return dumps(app_response)


if __name__ == "__main__":
    port = int(environ.get('PORT', 8080))
    app.run(port=port)
