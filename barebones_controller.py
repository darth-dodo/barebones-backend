from urllib.parse import parse_qs, urlparse


def four_oh_four_handler(request):
    parsed_path = urlparse(request.path)
    does_not_exist_message = f"Path {parsed_path.path} does not exist!"
    return {"message": does_not_exist_message}
