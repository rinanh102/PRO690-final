def test_status(app, client):
    res = client.get('/')
    assert res.status_code == 200