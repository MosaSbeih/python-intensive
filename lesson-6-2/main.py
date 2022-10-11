import logging
import os
import sys
import time
from uuid import uuid4

from manufacturer.computer import Computer
from manufacturer.conditioner import Conditioner
from manufacturer.smart_tv import SmartTV, SmartTV2
from manufacturer.smart_light import SmartLight, SmartLight2
from services.smart_house_service import SmartHouseService

# logging
LOG_FILE_NAME = "log.txt"
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(levelname)s | %(message)s"
level = os.environ.get("LOGLEVEL", DEFAULT_LOG_LEVEL)

# config
logging.basicConfig(filename=LOG_FILE_NAME, level=level, filemode='a', format=DEFAULT_LOG_FORMAT)
logger = logging.getLogger()

# console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(level)
console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
logger.addHandler(console_handler)


def main() -> None:
    smart_house = SmartHouseService()

    smart_house.register_devices(
        Computer(str(uuid4())),
        SmartLight(str(uuid4())),
        Conditioner(str(uuid4())),
        SmartTV(str(uuid4())),
        SmartTV2(str(uuid4())),
        SmartLight2(str(uuid4())),
    )

    logging.info(smart_house.monitoring_service.get_all_devices_serials(smart_house.devices))

    time.sleep(5)

    smart_house.start()

    time.sleep(5)

    smart_house.stop()


if __name__ == "__main__":
    main()
