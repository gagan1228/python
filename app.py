import json
import requests

url='https://574e-89-101-145-51.ngrok-free.app/churn_prediction'

input_data_for_model = {
    
   'SeniorCitizen': 1,
   'MonthlyCharges' : 74.4,
   'TotalCharges' : 306.6,
   'gender_Female': False,
   'gender_Male'   : True,
    'Partner_No'   : False,
    'Partner_Yes'  : True,
    'Dependents_No' : True,
    'Dependents_Yes' : False,
    'PhoneService_No' : False,
    'PhoneService_Yes' : True,
    'MultipleLines_No' : False,
    'MultipleLines_No_phone_service':False,
    'MultipleLines_Yes' : True,
    'InternetService_DSL': False,
    'InternetService_Fiber_optic': True,
    'InternetService_No' : False,
    'OnlineSecurity_No' : False,
    'OnlineSecurity_No_internet_service' : True,
    'OnlineSecurity_Yes' : False,
    'OnlineBackup_No' : True,
    'OnlineBackup_No_internet_service' : False,
    'OnlineBackup_Yes' : False,
    'DeviceProtection_No': False,
    'DeviceProtection_No_internet_service' : True,
    'DeviceProtection_Yes' : False,
    'TechSupport_No' : True,
    'TechSupport_No_internet_service' : False,
    'TechSupport_Yes': False,
    'StreamingTV_No' : True,
    'StreamingTV_No_internet_service' : False,
    'StreamingTV_Yes' : False,
    'StreamingMovies_No' :  True,
    'StreamingMovies_No_internet_service' : False,
    'StreamingMovies_Yes':False,
    'Contract_Month_to_month':True,
    'Contract_One_year' : False,
    'Contract_Two_year' : False,
    'PaperlessBilling_No' :  False,
    'PaperlessBilling_Yes': True,
    'PaymentMethod_Bank_transfer_automatic' : False,
    'PaymentMethod_Credit_card_automatic' : False,
    'PaymentMethod_Electronic_check' :  False,
    'PaymentMethod_Mailed_check' : True,
    'tenure_group_1_12' : True,
    'tenure_group_13_24':False,
    'tenure_group_25_36': False,
    'tenure_group_37_48': False,
    'tenure_group_49_60': False,
    'tenure_group_61_72': False,

    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)