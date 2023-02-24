from log_config import logger

def file_one_funcation():
    a = 2
    b = 0
    try:
        test = a / b
    except Exception as ex:
        # Provides stack trace.
        logger.exception(ex)
