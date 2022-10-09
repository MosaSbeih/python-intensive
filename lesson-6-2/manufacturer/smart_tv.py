import logging
from random import choice

from manufacturer.device import IDevice, ConnectionState, CHOICE_TUPLE


class SmartTV(IDevice):

    def __init__(self, serial_number: str) -> None:
        self.__serial_number = serial_number
        self.__device_state = ConnectionState.Disconnected

    def connect(self) -> bool:
        self.__device_state = choice(CHOICE_TUPLE)

        return self.__device_state.value

    def disconnect(self) -> bool:
        self.__device_state = choice(CHOICE_TUPLE)

        return self.__device_state.value

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_device_state(self) -> ConnectionState:
        return self.__device_state

    def switch_channel(self, channel_id: int) -> None:
        logging.info(f"Switched channel to {channel_id}")


class SmartTV2(IDevice):

    def __init__(self, serial_number: str) -> None:
        self.__serial_number = serial_number
        self.__device_state = ConnectionState.Disconnected

    def connect(self) -> bool:
        self.__device_state = choice(CHOICE_TUPLE)

        return self.__device_state.value

    def disconnect(self) -> bool:
        self.__device_state = choice(CHOICE_TUPLE)

        return self.__device_state.value

    def get_serial_number(self) -> str:
        return self.__serial_number

    def get_device_state(self) -> ConnectionState:
        return self.__device_state

    def switch_channel(self, channel_id: int) -> None:
        logging.info(f"Switched channel to {channel_id}")

    def blink_twice(self) -> None:
        logging.info(f"Blinked twice {self.__class__.__name__} ({self.__serial_number})")
