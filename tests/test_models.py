from rabbitmq_models.base_model import BaseModel
from rabbitmq_models.exceptions import InvalidSchemaError


class Dummy(BaseModel):
    REQUIRED_ATTRS = ['required_var']
    ACCEPTED_ATTRS = REQUIRED_ATTRS + ['non_req_var']

    def __init__(self, required_var, non_req_var=None):
        self.required_var = required_var
        self.non_req_var = non_req_var

    def __eq__(self, other):
        return self.required_var == other.required_var and self.non_req_var == other.non_req_var


def test_serialization_without_required_var_should_not_be_in_dict():
    expected_dict = {'required_var': 1}
    assert Dummy(required_var=1).serialize() == expected_dict


def test_deserialization_without_required_var_should_be_none():
    expected_dummy = Dummy(required_var=1)

    dummy: Dummy = Dummy.deserialize({'required_var': 1})

    assert expected_dummy.non_req_var is None
    assert dummy == expected_dummy


def test_serialization_deserialzation_should_equal_original_class():
    dummy = Dummy(required_var=1, non_req_var='Tank')

    assert dummy == Dummy.deserialize(dummy.serialize())


def test_deserialization_serialization_should_equal_original_dict():
    data = {'required_var': 2}

    assert data == Dummy.deserialize(data).serialize()


def test_deserialization_with_unwanted_attr_should_throw_InvalidSchemaError():
    data = {'required_var': 2, 'wtf': 3}

    try:
        Dummy.deserialize(data)
        assert False
    except InvalidSchemaError:
        assert True


def test_deserialization_with_missing_required_attr_should_throw_InvalidSchemaError():
    data = {'non_req_var': 3}

    try:
        Dummy.deserialize(data)
        assert False
    except InvalidSchemaError:
        assert True
