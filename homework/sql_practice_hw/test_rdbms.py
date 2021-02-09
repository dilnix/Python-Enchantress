import pytest
import psycopg2
from datetime import datetime
from homework.sql_practice_hw.rdbms import RDBMS


@pytest.fixture
def myDb():
    myDb = RDBMS()
    yield myDb
    myDb.cursor.close()
    myDb.connection.close()


existing_user = {
    'name': 'Illia',
    'email': 'illia.sukonnik@gmail.com',
    'registration_time': '2020-01-01 11:45:00'
}
addition_user = {
    'name': 'John',
    'email': 'john@example.com',
    'registration_time': '2021-02-04 23:34:56'
}
override_user = {
    'name': 'Travis',
    'email': 'travis@boringmail.com',
    'registration_time': '2021-02-04 23:45:59'
}
fake_user = {
    'name': 'Faker',
    'email': 'faker@gmail.com',
    'registration_time': 'unknown'
}


class TestCaseGood:

    def test_users(self, myDb):

        assert myDb.create_user(addition_user) == None
        self.user_id = myDb.get_latest_user_id()
        assert myDb.read_user_info(self.user_id) == (
            'John', 'john@example.com', datetime(2021, 2, 4, 23, 34, 56))
        myDb.update_user(override_user, self.user_id)
        assert myDb.read_user_info(self.user_id) == (
            'Travis', 'travis@boringmail.com', datetime(2021, 2, 4, 23, 45, 59))
        myDb.delete_user(self.user_id)
        assert myDb.read_user_info(self.user_id) == None

    def test_cart(self, myDb):

        myDb.create_user(addition_user)
        self.user_id = myDb.get_latest_user_id()
        self.addition_cart = {
            'creation_time': '2021-02-06 23:34:45',
            'user_id': self.user_id,
            'cart_details': [{'price': 800, 'product': 'Sport Bag'}]
        }
        myDb.create_cart(self.addition_cart)
        self.cart_id = myDb.get_latest_cart_id()

        assert myDb.read_cart(self.cart_id) == [
            (datetime(2021, 2, 6, 23, 34, 45), 'Sport Bag', 800)]

        self.override_cart = {
            'id': self.cart_id,
            'creation_time': '2021-02-06 23:34:56',
            'user_id': self.user_id,
            'cart_details': [
                {'cart_id': self.cart_id, 'price': 950, 'product': 'Sport Bag'},
                {'cart_id': self.cart_id, 'price': 1600, 'product': 'Lite Suite'}
            ]
        }
        myDb.update_cart(self.override_cart)

        assert myDb.read_cart(self.cart_id) == [
            (datetime(2021, 2, 6, 23, 34, 56), 'Sport Bag', 950),
            (datetime(2021, 2, 6, 23, 34, 56), 'Lite Suite', 1600)]

        myDb.delete_cart(self.cart_id)

        assert myDb.read_cart(self.cart_id) == []


class TestCaseBad:
    def test_users(self, myDb):

        self.fake_user_id = 10101
        pytest.raises(psycopg2.Error, lambda: myDb.create_user(existing_user))
        myDb.connection.commit()
        assert myDb.read_user_info(self.fake_user_id) == None
        pytest.raises(psycopg2.Error, lambda: myDb.update_user(fake_user, 3))
        myDb.connection.commit()
        pytest.raises(psycopg2.Error, lambda: myDb.delete_user(3))
        myDb.connection.commit()

    def test_cart(self, myDb):

        myDb.create_user(addition_user)
        self.user_id = myDb.get_latest_user_id()
        self.fake_cart = {
            'creation_time': 'not_a_datetime',
            'user_id': self.user_id,
            'cart_details': [{'price': 800, 'product': 'Sport Bag'}]
        }

        pytest.raises(psycopg2.Error, lambda: myDb.create_cart(self.fake_cart))
