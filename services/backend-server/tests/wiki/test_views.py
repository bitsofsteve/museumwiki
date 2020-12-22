import json
import pytest

from wiki.models import Wiki


@pytest.mark.django_db
def test_add_wiki(client, add_wiki):
    wiki = Wiki.objects.all()
    assert len(wiki) == 0

    response = client.post(
        "/api/v1/wiki/",
        {
            "name": "The British Museum",
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
    assert response.data["name"] == "The British Museum"
    wiki = Wiki.objects.all()
    assert len(wiki) == 1


@pytest.mark.django_db
def test_add_wiki_invalid_json(client):
    wiki = Wiki.objects.all()
    assert len(wiki) == 0

    response = client.post(
        "/api/v1/wiki/",
        {},
        content_type='application/json'
    )
    assert response.status_code == 400
    wiki = Wiki.objects.all()
    assert len(wiki) == 0


@pytest.mark.django_db
def test_get_single_wiki(client):
    wiki = add_wiki(name="Louvre Musueum", established="1793", city="Paris",
                    country="France", collection_size="380,000", visitors="9,600,000", website="www.louvre.fr")
    response = client.get(f"/api/v1/wiki/{wiki.id}/")
    assert response.status_code == 200
    assert response.data['name'] == "Louvre Musueum"


def test_get_single_wiki_wrong_id(client):
    response = client.get(f"/api/v1/wiki/bar/")
    assert response.status_code == 404
