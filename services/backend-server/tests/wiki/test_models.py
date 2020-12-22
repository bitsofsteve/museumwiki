import pytest

from wiki.models import Wiki


@pytest.mark.django_db
def test_wiki_model():
    wiki = Wiki(
        name="The British Musuem",
        established="1753",
        city="London",
        country="England",
        collection_size="8 million objects",
        visitors="6,239,983",
        website="www.britishmuseum.org",
    )
    wiki.save()
    assert wiki.name == "The British Musuem"
    assert wiki.established == "1753"
    assert wiki.city == "London"
    assert wiki.country == "England"
    assert wiki.collection_size == "8 million objects"
    assert wiki.visitors == "6,239,983"
    assert wiki.website == "www.britishmuseum.org"
    assert wiki.created_date
    assert wiki.updated_date
    assert str(wiki) == wiki.name
