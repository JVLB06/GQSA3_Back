from pydantic import BaseModel

class ViewDonationModel(BaseModel):
    DonorName: str
    ReceiverName: str
    Amount: float
    Date: str
    ProductName: str