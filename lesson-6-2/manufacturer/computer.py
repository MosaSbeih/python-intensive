from random import choice

from manufacturer.device import IDevice, ConnectionState, CHOICE_TUPLE


class Computer(IDevice):

    def __init__(self, serial_number):
        self.__serial_number = serial_number
        self.__device_state = ConnectionState.Disconnected
        self.hybernate_state = False

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

    def hybernate(self, state: bool = True) -> None:
        if state:
            self.hybernate_state = True
        else:
            self.hybernate_state = False
