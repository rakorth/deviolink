class ErrorMessage:
    def __init__(self, msg: str, err_type: str):
        self.msg = msg
        self.err_type = err_type

    def to_dict(self):
        return {
            '__type': 'err_message',
            'msg': self.msg
        }
