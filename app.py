import psycopg2
import uvicorn
from fastapi import FastAPI
from typing import List
from models.account import Account
from models.customer import Customer
from services.accountService import AccountService
from repositories.accountRepository import AccountRepository
from repositories.customerRepository import CustomerRepository
from services.customerService import CustomerService

app = FastAPI()
accountRepository = AccountRepository()
customerRepository = CustomerRepository()
accountService = AccountService(customerRepository, accountRepository)
customerService = CustomerService(customerRepository)

@app.post('/api/bankAccount/new')
async def createBankAccount(account: Account): #{'accountNumber': 'something','currentBalance':25,'customerId':1}
    #TODO: create bank account -> customer and address, min balance of 25
    return accountService.addNew(account)

@app.post('/api/Customer/new')
async def createCustomer(customer: Customer):
    return customerService.addNew(customer)

# @app.route('/api/Customer/new')
# async def createCustomer(customer: Customer):
#     return customerService.addNew(customer)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True,
            timeout_keep_alive=3600, workers=10)
    # connection = psycopg2.connect(
    # host="localhost",
    # database="capstone",
    # user="postgres",
    # password="password123"
    # )
    # connection.set_session(autocommit=True)
    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM account')
    #     result = cursor.fetchone()
    #     print(result)