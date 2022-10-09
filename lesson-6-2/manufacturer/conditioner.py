import logging
from enum import Enum
from random import choice

from manufacturer.device import IDevice, ConnectionState, CHOICE_TUPLE


class ConditionerModes(Enum):

    Normal = 1
    Heat = 2
    Rain = 3
    Turbo = 4
    Night = 5


class Conditioner(IDevice):

    def __init__(self, serial_number: str) -> None:
        self.__serial_number = serial_number
        self.__device_state = ConnectionState.Disconnected
        self.mode = ConditionerModes.Normal

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

    def switch_program(self, program_mode: ConditionerModes) -> None:
        self.mode = program_mode

        logging.info(f"Switched program to {self.mode.name}")
