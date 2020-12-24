import pytest
from wiki.models import Wiki


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


@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """
    Get rid of whitenoise "No directory at" warning, as it's not helpful when running tests.

    Related:
        - https://github.com/evansd/whitenoise/issues/215
        - https://github.com/evansd/whitenoise/issues/191
        - https://github.com/evansd/whitenoise/commit/4204494d44213f7a51229de8bc224cf6d84c01eb
    """
    settings.WHITENOISE_AUTOREFRESH = True
    