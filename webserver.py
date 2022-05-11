from wsgiref.simple_server import make_server

import falcon
import redis

from settings import REDIS_URL

r = redis.from_url(REDIS_URL)


class FartReturner:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML
        resp.text = f"""
        <html>
            <body>
            <title>Number of Items in Redis (probably)</title>
                <p>{r.dbsize()}</p>
            </body>
        </html>
        """


if __name__ == "__main__":
    app = falcon.App()
    app.add_route("/hypercounter", FartReturner())
    with make_server("", 6502, app) as httpd:
        print("Serving on port 6502")
        httpd.serve_forever()
