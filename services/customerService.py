from repositories.customerRepository import CustomerRepository
from models.customer import Customer

class CustomerService():
    def __init__(self, customerRepository: CustomerRepository):
        self.customerRepository = customerRepository

    def addNew(self, customer: Customer):
        return self.customerRepository.insert(customer)
    
    def getOne(self, customerNumber):
        return self.customerRepository.getByNumber(customerNumber)