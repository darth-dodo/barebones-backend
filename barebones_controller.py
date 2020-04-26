from urllib.parse import parse_qs, urlparse


def four_oh_four_handler(request):
    """Generic 404 handler which returns payload for JSON response"""
    parsed_path = urlparse(request.path)
    does_not_exist_message = f"Path {parsed_path.path} does not exist!"
    return {"message": does_not_exist_message}


def index(request):
    """Index controller which returns an HTML string for the HTML response parser"""
    query_components = parse_qs(urlparse(request.path).query)
    favorite_tree = None

    if "favoriteTree" in query_components:
        favorite_tree = query_components["favoriteTree"][0]

    if favorite_tree:
        html = f"<html><head></head><body><h1>It's nice to know that your favorite tree is a {favorite_tree}</h1></body></html>"
    else:
        html = f"<html><head></head><body><h1>Please tell me your favorite tree</h1></body></html>"

    return html
