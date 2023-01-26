from models.address import Address
from models.customer import Customer
from repositories.addressRepository import AddressRepository
import psycopg2

addressRepository = AddressRepository()

class CustomerRepository():
    def insert(self, customer: Customer):
        connection = psycopg2.connect(
        host="localhost",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO customer
                    (FirstName, LastName, AddressID, Email) VALUES
                    (%(FirstName)s, %(LastName)s, %(AddressID)s, %(Email)s)
                RETURNING ID
                """, {
                    'FirstName': customer.firstName,
                    'LastName': customer.lastName,
                    'AddressID' : customer.address.id, 
                    'Email' : customer.email
                }
            )
            customer.id = cursor.fetchone()[0]
            return customer

    def getOne(self, customerNumber):
        connection = psycopg2.connect(
        host="localhost",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT id, firstName, lastName, AddressID, Email FROM customer WHERE ID=(%s);', [customerNumber])
            result = cursor.fetchone()
            address = Address(id=result[3], address='', city='', state='', zipCode='')
        return Customer(id=result[0], firstName=result[1], lastName=result[2], address=address, email=result[4])