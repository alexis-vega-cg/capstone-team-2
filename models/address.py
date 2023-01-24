from pydantic import BaseModel

class Address(BaseModel):
    id: int
    address: str
    city: str
    state: str
    zipCode: str

    def __eq__(self, other):
        return self.id == other.id and self.address == other.address and \
        self.city == other.city and self.state == other.state and \
        self.zipCode == other.zipCode 