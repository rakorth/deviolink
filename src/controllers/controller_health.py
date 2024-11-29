import json

from adafruit_httpserver import Request, Response

import error_handler
from services import service_system


### --------------------------------------
### Controller for health endpoints
### --------------------------------------

def health_endpoint(request: Request) -> Response:
    try:
        response = json.dumps(service_system.get_hardware_status())
        return Response(request, response, content_type="application/json")
    except Exception as e:
        return error_handler.handle_http_error(request, e)
