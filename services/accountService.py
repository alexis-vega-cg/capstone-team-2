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