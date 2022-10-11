import logging

from manufacturer.device import IDevice, ConnectionState


class SmartLight(IDevice):

    def __init__(self, serial_number: str) -> None:
        self.__serial_number = serial_number
        self.__device_state = ConnectionState.Disconnected

    def connect(self) -> bool:
        self.__device_state = ConnectionState.random_item()

        return self.__device_state.value

    def disconnect(self) -> bool:
        self.__device_state = ConnectionState.random_item()

        return self.__device_state.value

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_device_state(self) -> ConnectionState:
        return self.__device_state

    def switch_light(self, light_color: str) -> None:
        logging.info(f"Light switched to {light_color}")


class SmartLight2(IDevice):

    def __init__(self, serial_number: str) -> None:
        self.__serial_number = serial_number
        self.__device_state = ConnectionState.Disconnected

    def connect(self) -> bool:
        self.__device_state = ConnectionState.random_item()

        return self.__device_state.value

    def disconnect(self) -> bool:
        self.__device_state = ConnectionState.random_item()

        return self.__device_state.value

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_device_state(self) -> ConnectionState:
        return self.__device_state

    def switch_light(self, light_color: str):
        logging.info(f"Light switched to {light_color}")

    def blink_twice(self) -> None:
        logging.info(f"Blinked twice {self.__class__.__name__} ({self.__serial_number})")
