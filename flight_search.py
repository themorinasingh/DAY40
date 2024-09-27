import requests

APIKEY = "YOUR API KEY/TOKEN"
API_SECRET = "YOUR API KEY/TOKEN"
TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'

class FlightSearch:
    def __init__(self):
        self._api_key = APIKEY
        self._api_secret = API_SECRET
        self._token = self._get_new_token()
        self.origin = "YYZ"

    def update_data(self, data):
        get_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        get_params = {
            'keyword': data['city'],
            'include': 'AIRPORTS'
        }
        headers = {
            'clientId': APIKEY,
            'clientSecret': API_SECRET,
            'Authorization': f'Bearer {self._token}'
        }
        response = requests.get(url=get_url, params=get_params, headers=headers)
        data['iataCode'] = response.json()['data'][0]['iataCode']



    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()['access_token']

    def check_flights(self, data, departure_date, return_date, is_direct='true'):
        base_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers?'
        params = {
            'originLocationCode': self.origin,
            'destinationLocationCode': data['iataCode'],
            'departureDate' : departure_date,
            'returnDate':return_date,
            'adults':'1',
            "nonStop": is_direct,
            "currencyCode": "CAD",
            'max' : '10'
        }
        headers = {
            'clientId': APIKEY,
            'clientSecret': API_SECRET,
            'Authorization': f'Bearer {self._token}'
        }

        response = requests.get(url=base_url, params=params, headers=headers)
        return response.json()

