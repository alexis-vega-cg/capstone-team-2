from dataclasses import dataclass
from models.account import Account
import psycopg2

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
