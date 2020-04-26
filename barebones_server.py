from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
from urllib.parse import parse_qs, urlparse
from socketserver import ThreadingMixIn


HTTP_METHOD_NOT_ALLOWED = 405


class BareBonesServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # set the status code
        self.send_response(200)

        # json response
        # set the headers and end headers
        # self.send_header("Content-type", "application/json")
        # self.end_headers()
        # payload = {"echo": "load and clear"}
        #
        # # provide the payload
        # self.wfile.write(bytes(json.dumps(payload), "utf-8"))

        # html response
        self.send_header("Content-type", "text/html")
        self.end_headers()

        query_components = parse_qs(urlparse(self.path).query)
        favorite_tree = None

        if "favoriteTree" in query_components:
            favorite_tree = query_components["favoriteTree"][0]

        if favorite_tree:
            html = f"<html><head></head><body><h1>It's nice to know that your favorite tree is a {favorite_tree}</h1></body></html>"
        else:
            html = f"<html><head></head><body><h1>Please tell me your favorite tree</h1></body></html>"

        self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)

    def do_PUT(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)

    def do_PATCH(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)

    def do_DELETE(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

    pass


if __name__ == "__main__":
    server = ThreadedHTTPServer(("0.0.0.0", 8000), BareBonesServerRequestHandler)

    try:
        server_info_message = f"\n\n\tStarting the server at {server.server_address} on {time.asctime()}\n\n"
        print(server_info_message)
        server.serve_forever()
    except KeyboardInterrupt:
        server_close_message = f"\n\n\tShutting down the server on {time.asctime()}\n\n"
        print(server_close_message)
        server.server_close()
