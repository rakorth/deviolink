import json

from adafruit_httpserver import Request, Response

import error_handler
from services import service_system


### --------------------------------------
### Controller for managing system config
### --------------------------------------

def system_info_endpoint(request: Request) -> Response:
    try:
        response = json.dumps(service_system.get_system_info().to_dict())
        return Response(request, response, content_type="application/json")
    except Exception as e:
        return error_handler.handle_http_error(request, e)


def get_device_config_endpoint(request: Request) -> Response:
    try:
        response = json.dumps(service_system.get_device_config().to_dict())
        return Response(request, response, content_type="application/json")
    except Exception as e:
        return error_handler.handle_http_error(request, e)


def update_system_config_endpoint(request: Request) -> Response:
    try:
        body = request.json()
        config = service_system.DeviceConfig(**body)
        service_system.save_device_config(config)
        response = json.dumps(config)
        return Response(request, response, content_type="application/json")
    except Exception as e:
        return error_handler.handle_http_error(request, e)
