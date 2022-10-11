from abc import ABC, abstractmethod
from enum import Enum
from random import choice


class ConnectionState(Enum):
    Connected = True
    Disconnected = False

    @staticmethod
    def random_item() -> "ConnectionState":
        return choice(list(ConnectionState))


class IDevice(ABC):

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        pass

    @abstractmethod
    def get_serial_number(self) -> str:
        pass

    @abstractmethod
    def get_device_state(self) -> ConnectionState:
        pass
