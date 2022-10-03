from fileinput import filename
from stat import filemode
import os
import sys
import colorlog


FILE_NAME = "log.txt"
LOG_LEVEL = colorlog.DEBUG
LOG_FORAMT = "%(log_color)s%(levelname)s | %(message)s"
LOG_COLORS ={
            "DEBUG": "blue",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "purple",
            }       

level = os.environ.get("LOGLEVEL", LOG_LEVEL)

colorlog.basicConfig(filename=FILE_NAME, log_colors=LOG_COLORS, level=level, filemode='a', format=LOG_FORAMT)

console_handler = colorlog.StreamHandler(sys.stdout)
console_handler.setLevel(level)
console_handler.setFormatter(colorlog.ColoredFormatter(fmt=LOG_FORAMT, log_colors=LOG_COLORS))



class ColorLog:

    def __init__(self) -> None:
        self.logger = colorlog.getLogger()
        self.logger.addHandler(console_handler)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)


if __name__ == "__main__":
      
    color1 = ColorLog()
    color1.debug("debug")
    color1.info("info")
    color1.warning("warning")
    color1.error("error")
    color1.critical("critical")
