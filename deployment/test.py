import requests


df = {
    "checking_status": 21,            
    "duration": 0,  
    "credit_history": 630,      
    "purpose": 1,
    "credit_amount": 13,
    "savings_status": 4,
    "employment": 2,
    "installment_commitment": 1,
    "personal_status": 1,
    "other_parties": 2,
    "residence_since": 2,
    "property_magnitude": 1,
    "age": 2, 
    "other_payment_pla":1,
    "housing": 1,
    "existing_credits": 2,
    "job": 0,
    "num_dependents": 0, 
    "own_telephone": 2,
    "foreign_worker": 2
}

# data=[[21,   0, 630,   1,  13,   4,   2,   1,   1,   2,   2,   1,   2,
#          1,   1,   2,   0,   0,   2,   2]]
#

link = 'http://localhost:9696/predict'
response = requests.post(link, json = df)
print(response.json())