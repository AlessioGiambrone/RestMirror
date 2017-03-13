# RestMirror

A simple app that will show the request headers and body after an HTTP request.

It can also easily put it on [Heroku](www.heroku.com).

## Usage

Start the server with

```bash
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

In response to a request, the app will return a JSON containing
  - an `headers` object
  - an `args` object with the URL parameters
  - a `data` object with the raw post body
  - a `file` object

## Development notes

### TODOs

- tests
