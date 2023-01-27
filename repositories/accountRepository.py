from audioop import add
from dataclasses import dataclass
from models.account import Account
from models.customer import Customer
from models.address import Address
from repositories.customerRepository import CustomerRepository
import psycopg2

customerRepository = CustomerRepository()

class AccountRepository():
    host = "capstone-team2-aexv.ckokfd9swhyk.us-west-2.rds.amazonaws.com"
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
    
    def getOneByAccountNumber(self, accountNumber):
        connection = psycopg2.connect(
        host="capstone-team2-aexv.ckokfd9swhyk.us-west-2.rds.amazonaws.com",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT id, AccountNumber,CustomerID, CurrentBalance FROM account WHERE AccountNumber=(%s);', [accountNumber])
            result = cursor.fetchone()
            try:
                address = Address(id=0, address='', city='', state='', zipCode='')
                customer = Customer(id=result[2], firstName='', lastName='', address= address, email='')
            except:
                return None
        return Account(id=result[0], accountNumber=result[1], customer=customer, currentBalance=result[3])

    def depositIntoAccount(self, accountNumber, deposit):
        connection = psycopg2.connect(
        host="capstone-team2-aexv.ckokfd9swhyk.us-west-2.rds.amazonaws.com",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute('UPDATE account SET CurrentBalance = CurrentBalance  + (%s) WHERE AccountNumber=(%s);', [deposit, accountNumber])
    
    def withdrawFromAccount(self, accountNumber,withdraw):
        connection = psycopg2.connect(
        host="capstone-team2-aexv.ckokfd9swhyk.us-west-2.rds.amazonaws.com",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute('UPDATE account SET CurrentBalance = CurrentBalance  - (%s) WHERE AccountNumber=(%s);', [withdraw, accountNumber])
    
    def closeAccount(self, accountNumber):
        connection = psycopg2.connect(
        host="capstone-team2-aexv.ckokfd9swhyk.us-west-2.rds.amazonaws.com",
        database="capstone",
        user="postgres",
        password="password123"
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM account WHERE AccountNumber=(%s) RETURNING *;', [accountNumber])
            accountResult = cursor.fetchone()

            customerId = accountResult[2]
            cursor.execute('DELETE FROM customer WHERE id=(%s) RETURNING *;', [customerId])
            customerResult = cursor.fetchone()

            addressId = customerResult[3]
            cursor.execute('DELETE FROM address WHERE id=(%s) RETURNING *;', [addressId])