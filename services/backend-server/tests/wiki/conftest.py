import pytest
from wiki.models import Wiki
import functools


@pytest.fixture(scope="function")
def add_wiki():
    def _add_wiki(name, established, city, country, collection_size, visitors, website):
        wiki = Wiki.objects.create(
            name=name,
            established=established,
            city=city,
            country=country,
            collection_size=collection_size,
            visitors=visitors,
            website=website,
        )
        return wiki

    return _add_wiki


@pytest.fixture
def client(client):
    client.get = functools.partial(client.get, secure=True)
    client.post = functools.partial(client.post, secure=True)
    client.put = functools.partial(client.put, secure=True)
    client.delete = functools.partial(client.delete, secure=True)
    return client
