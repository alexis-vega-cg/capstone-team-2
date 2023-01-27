import psycopg2
import uvicorn
from fastapi import FastAPI
from typing import List
from models.account import Account
from models.address import Address
from models.customer import Customer
from repositories.addressRepository import AddressRepository
from repositories.accountRepository import AccountRepository
from repositories.customerRepository import CustomerRepository
from services.accountService import AccountService
from services.addressService import AddressService
from services.customerService import CustomerService
from typing import List



app = FastAPI()
accountRepository = AccountRepository()
customerRepository = CustomerRepository()
addressRepository = AddressRepository()

accountService = AccountService(accountRepository, customerRepository, addressRepository)
customerService = CustomerService(customerRepository, addressRepository)
addressService = AddressService(addressRepository)

@app.post('/api/bankAccount/new')
async def createBankAccount(account: Account): 
    return accountService.addNew(account)

@app.get('/api/bankAccount/', response_model = List[Account])
async def getAllBankAccounts():
    return accountService.getAll()


@app.get('/api/bankAccount/{id}')
async def getBankAccountById(accountNumber):
    return accountService.getOneByAccountNumber(accountNumber)

@app.post('/api/bankAccount/deposit/{id}')
async def depositIntoAccount(accountNumber, deposit: float):
    return accountService.depositIntoAccount(accountNumber, deposit)

@app.post('/api/bankAccount/withdraw/{id}')
async def withdrawFromAccount(accountNumber, withdraw: float):
    return accountService.withdrawFromAccount(accountNumber, withdraw)

@app.post('/api/bankAccount/close/{id}')
async def closeAccount(accountNumber):
    return accountService.closeAccount(accountNumber)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True,
            timeout_keep_alive=3600, workers=10)