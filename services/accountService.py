import re
from repositories.accountRepository import AccountRepository
from repositories.customerRepository import CustomerRepository
from repositories.addressRepository import AddressRepository
from models.account import Account

class AccountService():
    def __init__(self, accountRepository: AccountRepository, customerRepository: CustomerRepository, addressRepository: AddressRepository):
        self.customerRepository = customerRepository
        self.addressRepository = addressRepository
        self.accountRepository = accountRepository

    def addNew(self, account: Account):
        address = self.addressRepository.insert(account.customer.address)
        account.customer.address = address
        customer = self.customerRepository.insert(account.customer)
        account.customer = customer
        return self.accountRepository.insert(account)

    def getAll(self):
        result = self.accountRepository.getAll()
        for account in result: 
            account.customer = self.customerRepository.getOne(account.customer.id)
            account.customer.address = self.addressRepository.getOne(account.customer.address.id)
        return result