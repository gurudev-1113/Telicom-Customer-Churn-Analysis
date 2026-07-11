from pydantic import BaseModel


class CustomerData(BaseModel):

    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Complain: int
    SatisfactionScore: int
    CardType: str
    PointEarned: int