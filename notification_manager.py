import smtplib


EMAIL = "YOUR EMAIL"
PASSWORD = "zojt megh llag prok"

class NotificationManager:
    def __init__(self):
        self.message = ""

    def message_maker(self, flight_price, from_iata, to_iata, from_date, to_date):
        message = (
            f"Subject: Low Price Alert - Fly from {from_iata} to {to_iata} for ${flight_price}!\n\n"
            f"Dear Traveler,\n\n"
            f"We're excited to inform you about a special offer! You can fly from {from_iata} to {to_iata} for only ${flight_price}.\n"
            f"This great deal is available for travel between {from_date} and {to_date}.\n\n"
            f"Don't miss out on this opportunity to save on your next trip. Book your flight now and enjoy amazing savings!\n\n"
            f"Best regards,\n"
            f"Your Travel Team"
        )
        self.message = message

    def send_mail(self, flight_price, from_iata, to_iata, from_date, to_date, to_email):
        self.message_maker(flight_price, from_iata, to_iata, from_date, to_date)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=self.message)



