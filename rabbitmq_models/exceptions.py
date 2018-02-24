class RabbitMQModelsError(Exception):
    pass


class InvalidSchemaError(RabbitMQModelsError):
    """
        Schema is not respecting the model's schema definition
    """
    pass
