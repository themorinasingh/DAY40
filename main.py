#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager
#-----------------------------------------------------------------------------------#

my_spreadsheet = DataManager()
sheet_data = my_spreadsheet.sheet_data

#-----------------------------------------------------------------------------------#
flight_search = FlightSearch()
#   for sheet in sheet_data:
#       flight_search.update_data(sheet)
#       payload = {"price" : sheet}
#       my_spreadsheet.put_data(payload)

#-----------------------------------------------------------------------------------#

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")

#-----------------------------------------------------------------------------------#

flight_check = FlightData()
notification_manager = NotificationManager()

#-----------------------------------------------------------------------------------#

email_list = my_spreadsheet.get_customer_emails()

#-----------------------------------------------------------------------------------#
for data in sheet_data:

        flight_data = flight_search.check_flights(data, departure_date=tomorrow, return_date=six_month_from_today)
        # print(flight_data)
        num_flights = int(flight_data['meta']['count'])
        if num_flights < 1:
            flight_data = flight_search.check_flights(data, departure_date=tomorrow, return_date=six_month_from_today, is_direct='false')
            if flight_data is None:
                continue

        cheapest_flight = flight_check.find_cheapest_flight(flight_data)

        for email in email_list:
            notification_manager.send_mail(flight_price=cheapest_flight.price,
                                           from_iata=cheapest_flight.origin_airport,
                                           to_iata=cheapest_flight.destination_airport,
                                           from_date=cheapest_flight.out_date,
                                           to_date=cheapest_flight.return_date,
                                           to_email=email)


        print(cheapest_flight.price)
        print(cheapest_flight.origin_airport)
        print(cheapest_flight.destination_airport)
        print(cheapest_flight.out_date)
        print(cheapest_flight.return_date)
        print(cheapest_flight.stops)
        print("")












