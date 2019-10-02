# rabbitmq_models
JSON Model definitions for Harmonium and related applications

# Usage:

#### From JSON to model
```python
from rabbitmq_models.article import Article

Article.deserialize({'title': 'Hello'})
# returns <Article object at 0x102256470>
```

#### From model to JSON
```python
from rabbitmq_models.article import Article

article = Article(title='Hello')
article.serialize()
# returns { 'title': 'Helloa' }
```
