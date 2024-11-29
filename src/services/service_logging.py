import adafruit_logging as logging

### --------------------------------------
### Service for managing loggers in the system
### Ref: https://docs.circuitpython.org/projects/logging/en/latest/api.html
### Ref: https://learn.adafruit.com/a-logger-for-circuitpython
### --------------------------------------

# Logs generated from our services
log_names = []
log_levels = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG
}

def create_logger(name: str) -> logging.Logger:
    log_names.append(name)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger


def get_logger_names() -> list[str]:
    return log_names


def get_logger_levels() -> dict:
    l = dict()

    for log in log_names:
        l[log] = get_logger_level(log)
    return l


def get_logger_level(logger: str) -> str:
    level = logging.getLogger(logger).getEffectiveLevel()
    if level >= logging.CRITICAL:
        return 'CRITICAL'
    elif level >= logging.ERROR:
        return 'ERROR'
    elif level >= logging.WARNING:
        return 'WARNING'
    elif level >= logging.INFO:
        return 'INFO'
    elif level >= logging.DEBUG:
        return 'DEBUG'
    else:
        return 'NONE'


def set_logger_level(logger: str, level_str: str):
    l = logging.logger_cache[logger]
    level = log_levels.get(level_str, logging.INFO)
    l.setLevel(level)
