from abc import ABC, abstractmethod
from enum import Enum


class ConnectionState(Enum):
    Connected = True
    Disconnected = False


CHOICE_TUPLE = (ConnectionState.Connected, ConnectionState.Disconnected)


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
