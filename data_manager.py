import requests
from pprint import pprint

URL = 'https://api.sheety.co/"YOUR API KEY/TOKEN"/filghtDealsProject/prices'
PUTURL = 'https://api.sheety.co/"YOUR API KEY/TOKEN"/filghtDealsProject/prices/'



class DataManager:
    def __init__(self):
        self.sheet_data = self.get_data()

    def get_data(self):
        response = requests.get(url=URL)
        data = response.json()
        return data

    def put_data(self, payload):
        url = f"{PUTURL}{payload["price"]['id']}"
        response = requests.put(url=url, json=payload)

    def get_customer_emails(self):
        response = requests.get(url='https://api.sheety.co/"YOUR API KEY/TOKEN"/filghtDealsProject/userDatabase')
        customer_list = response.json()['userDatabase']
        user_emails  =  [customer['email'] for customer in customer_list]
        return user_emails

