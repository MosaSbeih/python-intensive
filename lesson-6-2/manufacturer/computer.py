import logging

from manufacturer.device import IDevice, ConnectionState


class Computer(IDevice):

    def __init__(self, serial_number):
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

    def hybernate(self) -> None:
        logging.info("Computer has been hybernated.")
