import dateutil.parser

from rabbitmq_models.base_model import BaseModel


class ReadArticle(BaseModel):
    REQUIRED_ATTRS = ['title', 'read_at']
    ACCEPTED_ATTRS = REQUIRED_ATTRS + ['url']

    def __init__(self, title, read_at, url=None):
        self.title = title
        self.url = url
        self.read_at = dateutil.parser.parse(read_at)
