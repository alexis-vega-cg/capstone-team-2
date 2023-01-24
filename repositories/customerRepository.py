
from models.customer import Customer
import psycopg2


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
            cursor.execute(
                'INSERT INTO customer (firstName, lastName, AddressID, Email) VALUES (%s,%s,%s,%s)',[customer.firstName, customer.lastName, customer.address.id, customer.email])
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
                'SELECT id, firstName, lastName, AddressID, Email FROM  WHERE ID=(%s);', [customerNumber])
            result = cursor.fetchone()
            return Customer(id=result[0], firstName=result[1], lastName=result[2], address=result[3], email=result[4])