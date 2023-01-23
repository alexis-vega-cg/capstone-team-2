from email.headerregistry import Address
from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    firstName: str
    lastName: str
    address: Address
    email: str
    