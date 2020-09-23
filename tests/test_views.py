def test_index(client):
    rv = client.get('/')
    assert 'Hello!' in rv.text
