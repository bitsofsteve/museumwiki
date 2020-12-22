import pytest
from wiki.models import Wiki



@pytest.fixture(scope='function')
def add_wiki():
    def _add_wiki(name, established, city, country, collection_size, visitors, website):
        wiki = Wiki.objects.create(name=name, established=established, city=city, country=country,
                                   collection_size=collection_size, visitors=visitors, website=website)
        return wiki
    return _add_wiki



