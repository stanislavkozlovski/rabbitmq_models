import dateutil.parser

from rabbitmq_models.base_model import BaseModel


class ReadArticle(BaseModel):
    EXCHANGE_NAME = 'articles.read'
    REQUIRED_ATTRS = ['title', 'read_at', 'site_name']
    ACCEPTED_ATTRS = REQUIRED_ATTRS + ['url']

    def __init__(self, site_name: str, title: str, read_at: str, url=None):
        self.site_name = site_name
        self.title = title
        self.url = url
        self.read_at = dateutil.parser.parse(read_at)
