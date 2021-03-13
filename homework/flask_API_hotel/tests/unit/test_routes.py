import pytest


@pytest.mark.parametrize(
    'url',
    (
        '/check-in',
        '/check-in/'
    )
)
def test_check_in(app, url):
    response = app.post(url, json='something')
    assert response.status_code == 200
