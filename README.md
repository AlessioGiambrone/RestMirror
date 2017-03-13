# RestMirror

A simple app that will show the request headers and body after an HTTP request.
It is useful when it is needed a service -maybe remote- that shows how it is 
  being called, showing even headers.

It will respond even at subpaths (e.g. `localhost:5000/a/b/c` is equal to
  `localhost:5000`).

It can also easily put on [Heroku](www.heroku.com).

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

## Example

```bash
curl -X PUT --data-binary '{"message": "This is not a pipe"}' http://127.0.0.1:5000/a?b=c
```
will result in 
```json
{
   "args": "{\"b\": \"c\"}",
   "headers": {"Accept": "*/*", "Host": "127.0.0.1:5000", "User-Agent": "curl/7.52.1", "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "33"},
   "files": {},
   "data": "{\"message\": \"This is not a pipe\"}"
}
```

## Development notes

### TODOs

- tests
