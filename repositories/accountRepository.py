from audioop import add
from dataclasses import dataclass
from models.account import Account
from models.customer import Customer
from models.address import Address
from repositories.customerRepository import CustomerRepository
import psycopg2

customerRepository = CustomerRepository()

class AccountRepository():
    host = "localhost"
    database = "capstone"
    user = "postgres"
    password = "password123"

    def insert (self, account: Account): 
        with psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password) as db: 
            with db.cursor() as cursor: 
                cursor.execute("""
                    INSERT INTO account 
                    (AccountNumber, CustomerID, CurrentBalance) VALUES
                    (%(accountNumber)s, %(customerID)s, %(currentBalance)s)
                    RETURNING ID
                    """, {
                        'accountNumber': account.accountNumber,
                        'customerID': account.customer.id,
                        'currentBalance' : account.currentBalance, 
                    }
                )
                account.id = cursor.fetchone()[0]
        return account

    def getAll(self):
        result = [] 
        with psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, AccountNumber, CustomerID, CurrentBalance FROM account
                    """)
                rows = cursor.fetchall()
                for row in rows:
                    address = Address(id=0, address='', city='', state='', zipCode='')
                    customer = Customer(id=row[2], firstName='', lastName='', address= address, email='')
                    result.append(Account(id=row[0], accountNumber=row[1], customer=customer, currentBalance=row[3]))
        return result