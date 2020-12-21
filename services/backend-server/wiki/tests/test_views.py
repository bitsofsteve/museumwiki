import json
import pytest

from wiki.models import Wiki


@pytest.mark.django_db
def test_add_wiki(client):
    wiki = Wiki.objects.all()
    assert len(wiki) == 0

    response = client.post(
        "/api/v1/wiki/",
        {
            "name": "The British Musuem",
            "established": "1753",
            "city": "London",
            "country": "England",
            "collection_size": "8 million objects",
            "visitors": "6,239,983",
            "website": "www.britishmuseum.org"
        },
        content_type='application/json'

    )
    assert response.status_code == 201
    assert response.data["name"] == "The British Musuem"
    wiki = Wiki.objects.all()
    assert len(wiki) ==1

