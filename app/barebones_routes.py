from app.barebones_controller import four_oh_four_handler, index

SIMPLE_ROUTER = {
    "/": {"name": "index", "handler": index, "content_type": "text/html"},
    "404": {
        "name": "404_handler",
        "handler": four_oh_four_handler,
        "content_type": "application/json",
    },
}
