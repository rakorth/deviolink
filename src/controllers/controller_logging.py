import json

from adafruit_httpserver import Request, Response

import error_handler
from services import service_logging


### --------------------------------------
### Controller for managing loggers
### --------------------------------------

def logging_details_endpoint(request: Request) -> Response:
    try:
        response = json.dumps(service_logging.get_logger_levels())
        return Response(request, response, content_type="application/json")
    except Exception as e:
        return error_handler.handle_http_error(request, e)


def update_logging_level(request: Request) -> Response:
    try:
        logging_name = request.query_params["name"]
        logging_level = request.query_params["level"]
        service_logging.set_logger_level(logging_name, logging_level)
        response = json.dumps(service_logging.get_logger_levels())
        return Response(request, response, content_type="application/json")
    except Exception as e:
        return error_handler.handle_http_error(request, e)
