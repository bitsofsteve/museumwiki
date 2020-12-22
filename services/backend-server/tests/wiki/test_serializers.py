from wiki.serializers import WikiSerializer


def test_valid_wiki_serializer():
    valid_serializer_data = {
        "name": "The British Musuem",
        "established": "1753",
        "city": "London",
        "country": "England",
        "collection_size": "8 million objects",
        "visitors": "6,239,983",
        "website": "www.britishmuseum.org"
    }

    serializer = WikiSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}

def test_invalid_wiki_serializer():
    invalid_serializer_data = {
        "name": "The British Musuem",
        "established": "1753",
        "city": "London",
        "country": "England",
        "collection_size": "8 million objects",
        "visitors": "6,239,983"
    }
    serializer = WikiSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"website": ["This field is required."]}
