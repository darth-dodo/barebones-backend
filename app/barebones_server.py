from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
from urllib import parse
from socketserver import ThreadingMixIn
from app.barebones_routes import SIMPLE_ROUTER

HTTP_STATUS_METHOD_NOT_ALLOWED = 405
HTTP_STATUS_OK = 200
HTTP_STATUS_DOES_NOT_EXIST = 404


class BareBonesServerRequestHandler(BaseHTTPRequestHandler):
    """
     - Entry point for the Request
     - Extract the routes from `SIMPLE_ROUTER` and execute the handler method logic
     - Provide the response to the `_response_parser` to generate the response based on header content type
     - 404 handler for invalid URLs
     - Blacklist HTTP verbs besides GET
    """

    def do_GET(self):

        # set the status as 200 by default
        response_status_code = HTTP_STATUS_OK

        # extract the path and try to find in the registered routes
        parsed_path = parse.urlparse(self.path)
        router = SIMPLE_ROUTER.get(parsed_path.path)

        # if the path cannot be matched to a route, forward it to the 404 handler and reset the status
        if not router:
            router = SIMPLE_ROUTER["404"]
            response_status_code = HTTP_STATUS_DOES_NOT_EXIST

        route_handler = router["handler"]
        route_content_type = router["content_type"]

        # execute the logic inside the handler (controller)
        payload = route_handler(self)

        # set the headers and pass the payload to the response parser
        self._set_response_headers(response_status_code, route_content_type)
        self._response_parser(payload, route_content_type)

    def do_POST(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)

    def do_PUT(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)

    def do_PATCH(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)

    def do_DELETE(self):
        self.send_error(HTTP_STATUS_METHOD_NOT_ALLOWED)

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


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

    pass


if __name__ == "__main__":
    server = ThreadedHTTPServer(("0.0.0.0", 8000), BareBonesServerRequestHandler)

    try:
        server_info_message = f"\n\n\tStarting the server at http://{server.server_address[0]}:{server.server_port} on {time.asctime()}\n\n"
        print(server_info_message)
        server.serve_forever()
    except KeyboardInterrupt:
        server_close_message = f"\n\n\tShutting down the server on {time.asctime()}\n\n"
        print(server_close_message)
        server.server_close()
