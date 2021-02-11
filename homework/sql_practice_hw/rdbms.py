import psycopg2

"""
Before executing this script, you should launch your docker
container with simple Postgres DB with following command:
docker run --rm -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=qwerty -e POSTGRES_USER=dilnix -d postgres
"""


class RDBMS():
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database='dilnix',
                user='dilnix',
                password='qwerty',
                host='localhost',
                port='5432'
            )
            self.cursor = self.connection.cursor()
            print("Successfully connected DB")
        except (Exception, psycopg2.Error) as error:
            print("Can't connect to the DB", error)
            self.connection = None
        finally:
            if self.connection != None:
                self.sqlfile = open('homework/sql_practice_hw/shop.sql', 'r')
                self.cursor.execute(self.sqlfile.read())
                self.connection.commit()
                print("Successfully filled DB with starting data")

    def get_latest_user_id(self):
        self.id_query = "SELECT id FROM users ORDER BY id DESC LIMIT 1;"
        self.cursor.execute(self.id_query)
        self.user_id = int(self.cursor.fetchone()[0])
        # print(self.user_id)
        return self.user_id

    def create_user(self, user_info: dict):
        self.main_query = "INSERT INTO users (name, email, registration_time) VALUES (%(name)s, %(email)s, %(registration_time)s);"
        self.cursor.execute(self.main_query, user_info)
        self.connection.commit()

    def read_user_info(self, _id: int):
        self.main_query = f"SELECT name, email, registration_time FROM users WHERE id={_id};"
        self.cursor.execute(self.main_query)
        return self.cursor.fetchone()

    def update_user(self, new_info: dict, _id: int):
        self.main_query = f"UPDATE users SET name=%(name)s, email=%(email)s, registration_time=%(registration_time)s WHERE id={_id};"
        self.cursor.execute(self.main_query, new_info)
        self.connection.commit()

    def delete_user(self, _id: int):
        self.main_query = f"DELETE FROM users WHERE id={_id};"
        self.cursor.execute(self.main_query)
        self.connection.commit()

    def get_latest_cart_id(self):
        self.id_query = "SELECT id FROM cart ORDER BY id DESC LIMIT 1;"
        self.cursor.execute(self.id_query)
        self.cart_id = int(self.cursor.fetchone()[0])
        # print(self.cart_id)
        return self.cart_id

    def create_cart(self, cart: dict):
        self.main_query = "INSERT INTO cart (creation_time, user_id) VALUES (%(creation_time)s, %(user_id)s);"
        self.cursor.execute(self.main_query, cart)
        self.cart_id = self.get_latest_cart_id()
        self.details_query = f"INSERT INTO cart_details (cart_id, price, product) VALUES ({self.cart_id}, %(price)s, %(product)s);"
        # print(cart['cart_details'])
        for item in cart['cart_details']:
            # print(item)
            self.cursor.execute(self.details_query, item)
        self.connection.commit()

    def read_cart(self, _id: int):
        self.main_query = f"SELECT cart.creation_time, cart_details.product, cart_details.price FROM cart LEFT JOIN cart_details ON cart.id=cart_details.cart_id WHERE cart.id={_id};"
        self.cursor.execute(self.main_query)
        self.cart = self.cursor.fetchall()
        # print(self.cart)
        return self.cart

    def update_cart(self, cart: dict):
        self.main_query = "UPDATE cart SET creation_time=%(creation_time)s, user_id=%(user_id)s WHERE id=%(id)s;"
        self.details_query = """
        UPDATE cart_details 
        SET price=%(price)s, product=%(product)s 
        WHERE cart_id=%(cart_id)s AND %(product)s IN (SELECT product FROM cart_details); 
        INSERT INTO cart_details (cart_id, price, product) 
        SELECT %(cart_id)s, %(price)s, %(product)s 
        WHERE %(product)s NOT IN (SELECT product FROM cart_details);
        """
        self.cursor.execute(self.main_query, cart)
        for item in cart['cart_details']:
            # print(cart['cart_details'])
            self.cursor.execute(self.details_query, item)
        self.connection.commit()

    def delete_cart(self, _id: int):
        self.main_query = f"DELETE FROM cart WHERE id={_id};"
        self.details_query = f"DELETE FROM cart_details WHERE cart_id={_id};"
        self.cursor.execute(self.details_query)
        self.cursor.execute(self.main_query)
        self.connection.commit()


if __name__ == '__main__':
    myDb = RDBMS()
    # myDb.get_latest_user_id()
    myDb.create_user({
        'name': 'John',
        'email': 'john@example.com',
        'registration_time': '2021-02-04 23:34:56'
    })
    # myDb.get_latest_user_id()
    # myDb.update_user({
    #     'name': 'Travis',
    #     'email': 'travis@boringmail.com',
    #     'registration_time': '2021-02-04 23:45:59'
    # }, 4)
    # myDb.delete_user(4)
    myDb.create_cart({
        'creation_time': '2021-02-06 23:34:45',
        'user_id': 4,
        'cart_details': [{'price': 800, 'product': 'Sport Bag'}]
    })
    myDb.update_cart({
        'id': 5,
        'creation_time': '2021-02-06 23:34:56',
        'user_id': 4,
        'cart_details': [
            {'cart_id': 5, 'price': 950, 'product': 'Sport Bag'},
            {'cart_id': 5, 'price': 1600, 'product': 'Lite Suite'}
        ]
    })
    myDb.read_cart(5)
    # myDb.get_latest_cart_id()
