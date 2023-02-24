from log_config import logger

def file_two_funcation():
    a = 2
    b = 0
    try:
        test = a / b
    except Exception as ex:
        # Does not provide stack trace
        logger.exception("Here is an ERROR logger!")

    logger.debug("Here is an DEBUG logger.")
    logger.warning("Here is an WARNING logger.")
    logger.info("Here is an INFO logger.")
