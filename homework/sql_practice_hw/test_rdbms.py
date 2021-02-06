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
