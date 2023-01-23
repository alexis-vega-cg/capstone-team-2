from pydantic import BaseModel
from models import Customer

class Account(BaseModel):
    id: int
    accountNumber: str
    customerId: int
    currentBalance: Customer
