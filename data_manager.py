import requests
from pprint import pprint

URL = 'https://api.sheety.co/{YOUR KEY}/filghtDealsProject/prices'
PUTURL = 'https://api.sheety.co/{YOUR KEY}/filghtDealsProject/prices/'



class DataManager:
    def __init__(self):
        self.sheet_data = self.get_data()['prices']

    def get_data(self):
        response = requests.get(url=URL)
        data = response.json()
        return data

    def put_data(self, payload):
        url = f"{PUTURL}{payload["price"]['id']}"
        response = requests.put(url=url, json=payload)

    def get_customer_emails(self):
        response = requests.get(url="https://api.sheety.co/{YOUR KEY}/filghtDealsProject/userDatabase")
        customer_list = response.json()['userDatabase']
        user_emails  =  [customer['email'] for customer in customer_list]
        return user_emails

test = DataManager()
print(test.get_data())
