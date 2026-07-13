from api.schema import CustomerData
from api.main import predict

customer_dict = {
  "CreditScore":650,
  "Geography":"France",
  "Gender":"Male",
  "Age":40,
  "Tenure":5,
  "Balance":60000,
  "NumOfProducts":2,
  "HasCrCard":1,
  "IsActiveMember":1,
  "EstimatedSalary":50000,
  "Complain":0,
  "SatisfactionScore":4,
  "CardType":"Gold",
  "PointEarned":500
}

customer = CustomerData(**customer_dict)
result = predict(customer)
print("Result:", result)
