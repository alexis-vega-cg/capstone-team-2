from models.address import Address
from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    firstName: str
    lastName: str
    address: Address
    email: str

    def __eq__(self, other):
        return self.id == other.id and self.firstName == other.firstName and \
        self.lastName == other.lastName and self.address == other.address and \
        self.email == other.email 
    