from datetime import datetime, date

from rabbitmq_models.exceptions import InvalidSchemaError


class BaseModel:
    REQUIRED_ATTRS = []
    ACCEPTED_ATTRS = REQUIRED_ATTRS + []

    def serialize(self) -> dict:
        data = {}

        for attribute, value in self.__dict__.items():
            if attribute in self.ACCEPTED_ATTRS and value is not None:
                if isinstance(value, (datetime, date)):
                    value = value.isoformat()
                data[attribute] = value

        return data

    @classmethod
    def deserialize(cls, data) -> 'BaseModel':
        cls._validate_data(data)
        return cls(**data)

    @classmethod
    def _validate_data(self, data: dict):
        for required_attr in self.REQUIRED_ATTRS:
            if required_attr not in data:
                raise InvalidSchemaError(f'Attribute {required_attr} is missing from data!')
        for attr in data.keys():
            if attr not in self.ACCEPTED_ATTRS:
                raise InvalidSchemaError(f'Attribute {attr} is not accepted!')
