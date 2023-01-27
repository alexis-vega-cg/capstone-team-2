import string
from repositories.accountRepository import AccountRepository
from repositories.customerRepository import CustomerRepository
from repositories.addressRepository import AddressRepository
from models.account import Account


class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload


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
        
        if (account.currentBalance<25) :
            return BadRequest('Balance must be greater than or equal to 25', 400, { 'ext': 1 })

        return self.accountRepository.insert(account)

    def getAll(self):
        result = self.accountRepository.getAll()
        for account in result: 
            account.customer = self.customerRepository.getOne(account.customer.id)
            account.customer.address = self.addressRepository.getOne(account.customer.address.id)
        return result
    
    def getOneByAccountNumber(self, accountNumber: string):
        account = self.accountRepository.getOneByAccountNumber(accountNumber)
        if account is None:
            return BadRequest('Account does not exist', 400, { 'ext': 1 })
        
        account.customer = self.customerRepository.getOne(account.customer.id)
        account.customer.address = self.addressRepository.getOne(account.customer.address.id)
        return account
    
    def depositIntoAccount(self, accountNumber: string, deposit: float):
        if (deposit < 0):
            return BadRequest('Deposit amount must be greater than 0', 400, { 'ext': 1 })
        self.accountRepository.depositIntoAccount(accountNumber,deposit)
        return self.getOneByAccountNumber(accountNumber)
    
    def withdrawFromAccount(self, accountNumber: string, withdraw: float):
        if (withdraw < 0):
            return BadRequest('Withdraw amount must be greater than 0', 400, { 'ext': 1 })

        account = self.getOneByAccountNumber(accountNumber)
        if (account.currentBalance - withdraw) < 0:
            return BadRequest('Cant withdraw more than the current balance.', 400, { 'ext': 1 })

        self.accountRepository.withdrawFromAccount(accountNumber,withdraw)
        return self.getOneByAccountNumber(accountNumber)
    
    def closeAccount(self, accountNumber: string):
        account = self.accountRepository.getOneByAccountNumber(accountNumber)
        if account is None:
            return BadRequest('Account does not exist', 400, { 'ext': 1 })
        account.customer = self.customerRepository.getOne(account.customer.id)
        account.customer.address = self.addressRepository.getOne(account.customer.address.id)
        self.accountRepository.closeAccount(accountNumber)
        return account