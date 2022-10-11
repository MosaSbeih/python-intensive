import logging
from typing import Protocol, Union, runtime_checkable

from manufacturer.device import IDevice, ConnectionState
from services.smart_house_monitoring_service import SmartHouseMonitoringService


@runtime_checkable
class IBlinkingDevice(Protocol):
    def blink_twice(self) -> None:
        ...


@runtime_checkable
class HybernateDevices(Protocol):
    def hybernate(self) -> None:
        ...


class SmartHouseService:

    devices: list[Union[IDevice, HybernateDevices, IBlinkingDevice]] = []

    def __init__(self) -> None:
        self.monitoring_service = SmartHouseMonitoringService

    def register_devices(self, *args: Union[IDevice, IBlinkingDevice, HybernateDevices]) -> None:
        for new_device in args:
            self.devices.append(new_device)

    def start(self) -> None:
        temp_list = []

        for device in self.devices:
            device.connect()
            if device.get_device_state() == ConnectionState.Disconnected:
                logging.warning(f"{device.__class__.__name__} ({device.get_serial_number()}) not connected")
            else:
                temp_list.append(device)

        self.devices = temp_list

        logging.info(f"Connected Devices:{self.devices}")

    def stop(self) -> None:
        for device in self.devices:
            serial_num_temp = device.get_serial_number()
            if isinstance(device, HybernateDevices):
                logging.info(
                    f"{device.__class__.__name__} ({serial_num_temp}) is hybernated and still connected to services")
            else:
                if isinstance(device, IBlinkingDevice):
                    device.blink_twice()
                logging.info(f"{device.__class__.__name__} ({device.get_serial_number()}) has been disconnected")
                device.disconnect()
