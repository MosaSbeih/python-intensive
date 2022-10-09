from manufacturer.device import IDevice, ConnectionState


class SmartHouseMonitoringService:

    @staticmethod
    def get_all_devices_serials(devices: list[IDevice]) -> list[str]:
        serial_number_list = []

        for device in devices:
            serial_number_list.append(device.get_serial_number())

        return serial_number_list

    @staticmethod
    def check_state(devices: list[IDevice], serial_number: str) -> ConnectionState:

        for device in devices:
            if device.get_serial_number() == serial_number:
                return device.get_device_state()
