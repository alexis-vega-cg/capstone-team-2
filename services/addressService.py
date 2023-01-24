from repositories.addressRepository import AddressRepository
from models.address import Address

class AddressService():
    def __init__(self, addressRepository: AddressRepository):
        self.addressRepository = addressRepository

    def addNew(self, address: Address):
        return self.addressRepository.insert(address)
    
    def getOne(self, addressNumber):
        return self.addressRepository.getOne(addressNumber)