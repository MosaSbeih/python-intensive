from dataclasses import dataclass


@dataclass
class PackageVersion:

    version: str


@dataclass
class PackageName:

    name: str


@dataclass
class PackageDate:

    date: str


@dataclass
class PackageDescription:

    description: str


@dataclass
class Package:

    def __init__(self, **kwargs) -> None:
        self.Package: dict = {
            "PackageName": kwargs["PackageName"].name,
            "PackageVersion": kwargs["PackageVersion"].version,
            "PackageDate": kwargs["PackageDate"].date,
            "PackageDescription": kwargs["PackageDescription"].description,
        }


DATA_NAMES = (PackageName.__name__, PackageVersion.__name__, PackageDate.__name__, PackageDescription.__name__)
