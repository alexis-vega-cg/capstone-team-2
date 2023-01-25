from models.address import Address
import psycopg2

class AddressRepository():
    def insert(self, address: Address):
        connection = psycopg2.connect(
        host="localhost",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute('''
             INSERT INTO address (Address, City, State, ZipCode) VALUES (%s,%s,%s,%s) 
             RETURNING ID
            ''',
            [address.address,address.city,address.state,address.zipCode]
            )
            address.id = cursor.fetchone()[0]
            return address

    def getOne(self, addressNumber):
        connection = psycopg2.connect(
        host="localhost",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT id, Address, City , State , ZipCode FROM address WHERE ID=(%s);', [addressNumber])
            result = cursor.fetchone()
            return Address(id=result[0], address=result[1], city=result[2], state=result[3], zipCode=result[4])