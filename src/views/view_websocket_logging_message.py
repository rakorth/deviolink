class LoggingWebsocketMessage:
    def __init__(self, log_name: str, log_level: str, msg: str):
        self.log_name = log_name
        self.log_level = log_level
        self.msg = msg

    def to_dict(self):
        return {
            '__type': 'log_message',
            'log_name': self.log_name,
            'log_level': self.log_level,
            'msg': self.msg
        }
