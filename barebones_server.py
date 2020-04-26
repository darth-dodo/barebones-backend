from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
from urllib.parse import parse_qs, urlparse
from urllib import parse
from socketserver import ThreadingMixIn
from routes import SIMPLE_ROUTER

HTTP_STATUS_METHOD_NOT_ALLOWED = 405
HTTP_STATUS_OK = 200


class BareBonesServerRequestHandler(BaseHTTPRequestHandler):
    def _set_response_headers(self, status_code, content_type):
        """Reusable method for setting the response headers"""
        self.send_response(status_code)

        # set the headers and end headers
        self.send_header("Content-type", content_type)
        self.end_headers()

    def _response_parser(self, payload, content_type):
        """Response Parser based on content_type"""
        if content_type == "application/json":
            self.wfile.write(bytes(json.dumps(payload), "utf-8"))
        elif content_type == "text/html":
            self.wfile.write(bytes(payload, "utf8"))

    def do_GET(self):

        parsed_path = parse.urlparse(self.path)
        router = SIMPLE_ROUTER.get(parsed_path.path)

        # if the path cannot be matched to a route, forward it to the 404 handler
        if not router:
            router = SIMPLE_ROUTER["404"]

        route_name = router["name"]
        route_handler = router["handler"]
        route_content_type = router["content_type"]

        payload = {"message": "This page does not exist!"}

        self._set_response_headers(HTTP_STATUS_OK, route_content_type)
        self._response_parser(payload, route_content_type)

        # query_components = parse_qs(urlparse(self.path).query)
        # favorite_tree = None
        #
        # if "favoriteTree" in query_components:
        #     favorite_tree = query_components["favoriteTree"][0]
        #
        # if favorite_tree:
        #     html = f"<html><head></head><body><h1>It's nice to know that your favorite tree is a {favorite_tree}</h1></body></html>"
        # else:
        #     html = f"<html><head></head><body><h1>Please tell me your favorite tree</h1></body></html>"
        #
        # self.wfile.write(bytes(html, "utf8"))

    def do_POST(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)

    def do_PUT(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)

    def do_PATCH(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)

    def do_DELETE(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)


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
