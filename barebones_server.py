from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time


HTTP_METHOD_NOT_ALLOWED = 405


class BareBonesServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # set the status code
        self.send_response(200)

        # set the headers and end headers
        self.send_header("Content-type", "application/json")
        self.end_headers()

        payload = {"echo": "load and clear"}

        # provide the payload
        self.wfile.write(bytes(json.dumps(payload), "utf-8"))

    def do_POST(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)

    def do_PUT(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)

    def do_PATCH(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)

    def do_DELETE(self):
        self.send_error(HTTP_METHOD_NOT_ALLOWED)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), BareBonesServerHandler)

    try:
        server_info_message = f"\n\n\tStarting the server at {server.server_address} on {time.asctime()}\n\n"
        print(server_info_message)
        server.serve_forever()
    except KeyboardInterrupt:
        server_close_message = f"\n\n\tShutting down the server on {time.asctime()}\n\n"
        print(server_close_message)
        server.server_close()
