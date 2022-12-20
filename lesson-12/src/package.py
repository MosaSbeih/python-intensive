from dataclasses import dataclass, fields


@dataclass
class Package:
    name: str
    version: str
    date: str
    description: str

    @classmethod
    def get_data_names(cls):
        return [field.name for field in fields(cls)]
