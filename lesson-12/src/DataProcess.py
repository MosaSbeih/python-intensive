from logging import Logger
from abc import ABC, abstractmethod
from json import dumps
from csv import DictWriter
from dict2xml import dict2xml


class PackageVersion:

    def __init__(self, version: str):
        self.__version = version

    def get(self) -> str:
        return self.__version


class PackageName:

    def __init__(self, name: str):
        self.__name = name

    def get(self) -> str:
        return self.__name


class PackageDate:

    def __init__(self, date: str):
        self.__date = date

    def get(self) -> str:
        return self.__date


class PackageDescription:

    def __init__(self, description: str):
        self.__description = description

    def get(self) -> str:
        return self.__description


class Package:

    def __init__(self, **kwargs):
        self.__info = kwargs

    def get(self):
        return self.__info


DATA_NAMES = (PackageName.__name__, PackageVersion.__name__, PackageDate.__name__, PackageDescription.__name__)


class IData(ABC):

    @abstractmethod
    def create(self, file_name: str) -> None:
        pass


class JSON(IData):

    def __init__(self, package_info: Package) -> None:
        self.__info = {key: package_info.get()[key].get() for key in package_info.get().keys()}

    def create(self, file_name: str) -> None:
        with open(file_name + ".json", "w", encoding="utf-8") as file:
            file.write(dumps(self.__info))


class CSV(IData):

    def __init__(self, package_info: Package) -> None:
        self.__info = {key: package_info.get()[key].get() for key in package_info.get().keys()}

    def create(self, file_name: str) -> None:
        with open(file_name + ".csv", "w", encoding="utf-8") as file:
            writer = DictWriter(file, DATA_NAMES)
            writer.writeheader()
            writer.writerow(self.__info)


class XML(IData):

    def __init__(self, package_info: Package) -> None:
        self.__info = {key: package_info.get()[key].get() for key in package_info.get().keys()}

    def create(self, file_name: str) -> None:
        with open(file_name + ".xml", "w", encoding="utf-8") as file:
            file.write(dict2xml(self.__info, wrap="package", indent="    "))


class CreateData:

    @staticmethod
    def create(date_type: str, file_name: str, logger: Logger, package_info: Package):
        if date_type == "json":
            logger.info("    Parsing data into json file...")
            obj = JSON(package_info)
            obj.create(file_name)
            logger.info("    Data was converted to json. Saving results to output")

        elif date_type == "csv":
            logger.info("    Parsing data into csv file...")
            obj = CSV(package_info)
            obj.create(file_name)
            logger.info("    Data was converted to csv. Saving results to output")

        elif date_type == "xml":
            logger.info("    Parsing data into xml file...")
            obj = XML(package_info)
            obj.create(file_name)
            logger.info("    Data was converted to xml. Saving results to output")
