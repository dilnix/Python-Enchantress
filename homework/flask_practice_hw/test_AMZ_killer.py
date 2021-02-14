from homework.flask_practice_hw.AMZ_killer import amz_killer as app
from freezegun import freeze_time
import pytest


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time('2021-02-08 14:16:41')
def test_create_user(store_app):
    response = store_app.post(
        '/users',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@gmail.com"
        })
    assert response.status_code == 201
    assert response.json == {
        "user_id": 1,
        "registration_timestamp": '2021-02-08T14:16:41'
    }

    user_id = response.json['user_id']
    response = store_app.get(f'/users/{user_id}')

    assert response.status_code == 200
    assert response.json == {
        "name": "Illia",
        "email": "illia.sukonnik@gmail.com",
        "user_id": user_id,
        "registration_timestamp": '2021-02-08T14:16:41'
    }


def test_get_user_no_such_user(store_app):
    response = store_app.get('/users/2')

    assert response.status_code == 404
    assert response.json == {
        "error": "no such user with id 2"
    }


def test_set_user(store_app):
    response = store_app.put(
        '/users/1',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@example.com",
        })

    assert response.status_code == 200

    response = store_app.put(
        '/users/3',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@example.com",
        })

    assert response.status_code == 404
    assert response.json == {
        "error": "no such user with id 3"
    }


def test_remove_user(store_app):
    response = store_app.delete('/users/1')

    assert response.status_code == 200

    response = store_app.delete('/users/3')

    assert response.status_code == 404
    assert response.json == {
        "error": "no such user with id 3"
    }
