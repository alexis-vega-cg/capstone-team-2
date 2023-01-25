from email.headerregistry import Address
from repositories.customerRepository import CustomerRepository
from repositories.addressRepository import AddressRepository
from models.customer import Customer

class CustomerService():
    def __init__(self, customerRepository: CustomerRepository, addressRepository: AddressRepository):
        self.customerRepository = customerRepository
        self.addressRepository = addressRepository

    def addNew(self, customer: Customer):
        address = self.addressRepository.insert(customer.address)
        customer.address = address
        return self.customerRepository.insert(customer)
    
    def getOne(self, customerNumber):
        return self.customerRepository.getByNumber(customerNumber)