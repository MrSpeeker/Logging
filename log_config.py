import logging

from rich.logging import RichHandler

from pathlib import Path
from datetime import datetime

class OneLineExceptionFormatter(logging.Formatter):
    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '\n\t\t\t\t\t\t\t')
        return s

# Here we create the header for the log file.
path = Path("test.log")
if path.is_file() == False:
    devider = "----------------------------------------------------------------------\n"
    project_name = "Project name              - Smart Matching\n"
    log_file_creation_date = "Creation date of log file - " + str(datetime.now()) + "\n"
    with open(file="test.log", mode="w") as file:
        file.write(devider)
        file.write(project_name)
        file.write(log_file_creation_date)
        file.write(devider)
        file.write("\n\n")

logger = logging.getLogger(__name__)

# The handler determines where the logs go: stdout/file.
shell_handler = RichHandler()
file_handler = logging.FileHandler("test.log")

logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.INFO)

# The formatter determines what our logs will look like.
fmt_shell = "%(message)s"
fmt_file = "%(asctime)s %(levelname)s\t(%(filename)s:%(lineno)d) - %(message)s"
fmt_date_file = "[%x %X]"

shell_formatter = logging.Formatter(fmt_shell)
file_formatter = OneLineExceptionFormatter(fmt=fmt_file, datefmt=fmt_date_file)

# Here we hook everything together.
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)


