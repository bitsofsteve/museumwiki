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
            "collection_size": "8,000,000",
            "visitors": "6,239,983",
            "website": "www.britishmuseum.org",
        },
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.data["name"] == "The British Museum"
    wiki = Wiki.objects.all()
    assert len(wiki) == 1


@pytest.mark.django_db
def test_add_wiki_invalid_json(client):
    wiki = Wiki.objects.all()
    assert len(wiki) == 0

    response = client.post("/api/v1/wiki/", {}, content_type="application/json")
    assert response.status_code == 400
    wiki = Wiki.objects.all()
    assert len(wiki) == 0


@pytest.mark.django_db
def test_get_single_wiki(client, add_wiki):
    wiki = add_wiki(
        name="Louvre Musueum",
        established="1793",
        city="Paris",
        country="France",
        collection_size="380,000",
        visitors="9,600,000",
        website="www.louvre.fr",
    )
    response = client.get(f"/api/v1/wiki/{wiki.id}/")
    assert response.status_code == 200
    assert response.data["name"] == "Louvre Musueum"


def test_get_single_wiki_wrong_id(client):
    response = client.get("/api/v1/wiki/bar/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_all_wiki(client, add_wiki):
    wiki_one = add_wiki(
        name="Louvre Musueum",
        established="1793",
        city="Paris",
        country="France",
        collection_size="380,000",
        visitors="9,600,000",
        website="www.louvre.fr",
    )
    wiki_two = add_wiki(
        name="The British Musueum",
        established="1753",
        city="London",
        country="England",
        collection_size="8,000,000",
        visitors="6,239,983",
        website="www.britishmusuem.org",
    )
    resp = client.get("/api/v1/wiki/")
    assert resp.status_code == 200
    assert resp.data[0]["name"] == wiki_one.name
    assert resp.data[1]["name"] == wiki_two.name


@pytest.mark.django_db
def test_delete_a_wiki(client, add_wiki):
    wiki = add_wiki(
        name="Louvre Musueum",
        established="1793",
        city="Paris",
        country="France",
        collection_size="380,000",
        visitors="9,600,000",
        website="www.louvre.fr",
    )

    resp_one = client.get(f"/api/v1/wiki/{wiki.id}/")
    assert resp_one.status_code == 200
    assert resp_one.data["name"] == "Louvre Musueum"

    resp_two = client.delete(f"/api/v1/wiki/{wiki.id}/")
    assert resp_two.status_code == 204

    resp_three = client.get(f"/api/v1/wiki/")
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0

@pytest.mark.django_db
def test_delete_wiki_wrong_id(client):
    resp = client.delete("/api/v1/wiki/100/")
    assert resp.status_code == 404
