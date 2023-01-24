from pydantic import BaseModel
from models.customer import Customer

class Account(BaseModel):
    id: int
    accountNumber: str
    customerId: int
    currentBalance: int

    def __eq__(self, other):
        return self.id == other.id and self.accountNumber == other.accountNumber and \
            self.customerId == other.customerId and self.currentBalance == other.currentBalance
