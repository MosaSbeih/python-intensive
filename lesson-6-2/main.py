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

if __name__ == "__main__":

    computer = Computer(str(uuid4()))
    conditioner = Conditioner(str(uuid4()))
    smart_tv = SmartTV(str(uuid4()))
    smart_tv2 = SmartTV2(str(uuid4()))
    smart_light = SmartLight(str(uuid4()))
    smart_light2 = SmartLight2(str(uuid4()))

    computer.connect()
    conditioner.connect()
    smart_tv.connect()
    smart_tv2.connect()
    smart_light.connect()
    smart_light2.connect()

    smart_house = SmartHouseService()
    smart_house.register_devices(computer, conditioner, smart_light, smart_tv, smart_light2, smart_tv2)

    serial_numbers_list = smart_house.monitoring_service.get_all_devices_serials(devices=smart_house.devices)
    check_state = smart_house.monitoring_service.check_state(devices=smart_house.devices,
                                                             serial_number=computer.get_serial_number())

    logging.info(f"serial numbers: {serial_numbers_list}")
    logging.info(f"{computer.__class__.__name__} ({computer.get_serial_number()}) state: {check_state}")

    smart_house.start()

    time.sleep(5)

    smart_house.stop()
