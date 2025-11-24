from pydantic import BaseModel

class DonationModel(BaseModel):
    DonorId: int
    ReceiverId: int
    Amount: float
    Date: str
    Message: str = None