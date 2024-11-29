import json
import traceback

from adafruit_httpserver import Request, Response, Status, Websocket

from services import service_logging as log_factory
from  views.view_error_message import ErrorMessage

logger = log_factory.create_logger("error_handler")


def handle_http_error(request: Request, ex: Exception) -> Response:
    msg = ErrorMessage(
        msg=str(ex),
        err_type=type(ex).__name__
    )

    body = json.dumps(msg.to_dict())

    return Response(request, body, content_type="application/json",
                    status=Status(code=500, text="Internal Server Error"))


def handle_websocket_error(websocket: Websocket, ex: Exception) -> None:
    msg = ErrorMessage(
        msg=str(ex),
        err_type=type(ex).__name__
    )

    websocket.send_message(json.dumps(msg.to_dict()), fail_silently=True)
