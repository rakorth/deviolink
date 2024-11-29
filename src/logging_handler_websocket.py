import json

import adafruit_logging as logging

import webserver
from views.view_websocket_logging_message import LoggingWebsocketMessage


class WebsocketHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        if webserver.websocket is not None:
            msg = LoggingWebsocketMessage(
                log_name=record.name,
                log_level=record.levelname,
                msg=record.msg,
            )
            try:
                webserver.websocket.send_message(json.dumps(msg.to_dict()), fail_silently=False)
            except Exception:
                pass
