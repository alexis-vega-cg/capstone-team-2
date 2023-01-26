from pydantic import BaseModel
from models.customer import Customer

class Account(BaseModel):
    id: int
    accountNumber: str
    customer: Customer
    currentBalance: int

    def __eq__(self, other):
            return self.id == other.id and self.accountNumber == other.accountNumber and \
                self.customer == other.customer and self.currentBalance == other.currentBalance
