import unittest
import threading
import time
from urllib import request as urllib_request
from urllib import parse
from urllib import error as urllib_error
from barebones_server import ThreadedHTTPServer, BareBonesServerRequestHandler


class TestBareBonesServerRequestHandler(unittest.TestCase):
    """
    - Run an instance of the server as a daemon for executing the test cases
    - Dynamically allocate a port free for the test server
    """

    def setUp(self):
        # dynamically bind the server to first available port
        self.test_server = ThreadedHTTPServer(
            ("localhost", 0), BareBonesServerRequestHandler
        )

        # assign the server to a separate thread
        self.server_thread = threading.Thread(target=self.test_server.serve_forever)

        # make the thread in a daemon
        self.server_thread.setDaemon(True)
        self.server_thread.start()

        # back-off while the server starts
        time.sleep(1)

        # application URLs
        self.root_url = f"http://{self.test_server.server_address[0]}:{self.test_server.server_port}/"

    def test_405_with_post_request(self):
        query_args = {"q": "query string", "foo": "bar"}
        try:
            urllib_request.urlopen(
                url=self.root_url, data=parse.urlencode(query_args).encode("utf-8"),
            )
        except urllib_error.HTTPError as response:
            assert response.code == 405
            assert response.msg == "Method Not Allowed"

    def test_405_for_all_the_other_verbs(self):
        """Out of scope"""
        pass

    def test_index_page_response_with_no_params(self):
        # send the request to the test server and decode the response
        response = urllib_request.urlopen(self.root_url)
        decoded_response = response.read().decode("utf-8")

        # assert the response to the required html
        default_response = "<html><head></head><body><h1>Please tell me your favorite tree</h1></body></html>"
        assert decoded_response == default_response

    def test_index_page_response_with_invalid_params(self):
        # create the required query params
        query_args = {"favoriteAnimal": "Tiger"}
        encoded_args = str(parse.urlencode(query_args))
        request_url = f"{self.root_url}?{encoded_args}"

        # send the request to the test server and decode the response
        response = urllib_request.urlopen(request_url)
        decoded_response = response.read().decode("utf-8")

        # assert the response to the required html
        default_response = "<html><head></head><body><h1>Please tell me your favorite tree</h1></body></html>"
        assert decoded_response == default_response

    def test_index_page_response_with_blank_favorite_tree_param(self):

        # create the required query params
        query_args = {"favoriteTree": ""}
        encoded_args = str(parse.urlencode(query_args))
        request_url = f"{self.root_url}?{encoded_args}"

        # send the request to the test server and decode the response
        response = urllib_request.urlopen(request_url)
        decoded_response = response.read().decode("utf-8")

        # assert the response to the required html
        default_response = "<html><head></head><body><h1>Please tell me your favorite tree</h1></body></html>"
        assert decoded_response == default_response

    def test_index_page_response_with_neem_tree_param(self):
        # create the required query params
        query_args = {"favoriteTree": "Neem"}
        encoded_args = str(parse.urlencode(query_args))
        request_url = f"{self.root_url}?{encoded_args}"

        # send the request to the test server and decode the response
        response = urllib_request.urlopen(request_url)
        decoded_response = response.read().decode("utf-8")

        # assert the response to the required html
        default_response = "<html><head></head><body><h1>It's nice to know that your favorite tree is a Neem</h1></body></html>"
        assert decoded_response == default_response
