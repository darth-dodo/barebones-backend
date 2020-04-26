from barebones_controller import four_oh_four_handler

SIMPLE_ROUTER = {
    "/": {"name": "index", "handler": None, "content_type": "text/html"},
    "404": {
        "name": "404_handler",
        "handler": four_oh_four_handler,
        "content_type": "application/json",
    },
}
