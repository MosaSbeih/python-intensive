import os


from logging import Logger
from abc import ABC, abstractmethod
from json import dumps
from csv import DictWriter
from dict2xml import dict2xml
from package import Package
from typing import Any


ABS_PATH = os.path.abspath("").replace("src", "")
OUTPUT_PATH = os.path.join(ABS_PATH, "output")


class IDataConverter(ABC):

    @staticmethod
    @abstractmethod
    def convert(output_file_name: str, logger: Logger, package_info: Package) -> None:
        pass


class JSONConverter(IDataConverter):

    @staticmethod
    def convert(output_file_name: str, logger: Logger, package_info: Package) -> None:
        try:
            logger.info("Parsing data into json file...")
            with open(output_file_name + ".json", "w", encoding="utf-8") as file:
                file.write(dumps(package_info.__dict__))
        except FileExistsError:
            logger.warning("File already exists, conversion failed")
        except FileNotFoundError:
            logger.warning("File path not found, conversion failed")
        else:
            logger.info("Data was converted to json. Saving results to output")


class CSVConverter(IDataConverter):

    @staticmethod
    def convert(output_file_name: str, logger: Logger, package_info: Package) -> None:
        try:
            logger.info("Parsing data into csv file...")
            with open(output_file_name + ".csv", "w", encoding="utf-8") as file:
                writer = DictWriter(file, Package.get_data_names())
                writer.writeheader()
                writer.writerow(package_info.__dict__)
        except FileExistsError:
            logger.warning("File already exists, conversion failed")
        except FileNotFoundError:
            logger.warning("File path not found, conversion failed")
        else:
            logger.info("Data was converted to csv. Saving results to output")


class XMLConverter(IDataConverter):

    @staticmethod
    def convert(output_file_name: str, logger: Logger, package_info: Package) -> None:
        try:
            logger.info("Parsing data into xml file...")
            with open(output_file_name + ".xml", "w", encoding="utf-8") as file:
                file.write(dict2xml(package_info.__dict__, wrap="package", indent="    "))
        except FileExistsError:
            logger.warning("File already exists, conversion failed")
        except FileNotFoundError:
            logger.warning("File path not found, conversion failed")
        else:
            logger.info("Data was converted to xml. Saving results to output")


class PackageConverter:

    @staticmethod
    def convert(data_type: Any, output_file_name: str, logger: Logger, package_info: Package) -> None:
        data_type.convert(output_file_name, logger, package_info)
