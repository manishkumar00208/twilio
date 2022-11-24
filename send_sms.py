import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# account_sid = os.getenv('AC3870e9de6dda09a9989d89f0a00c67e3')
# auth_token = os.getenv('0e328f21ca61dd6c0f6cd847c7bc94b0')
client = Client('ACf5d67d5fb59512b987373de070a23a9f', '256cece344ed354504dcee09b715f868')

message = client.messages \
    .create(
        body="Hi",
        from_='+15627845803',
        media_url=['https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRed_soil&psig=AOvVaw0vaMqRJm0ni5R393Uetui8&ust=1669349293150000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLit6O74xfsCFQAAAAAdAAAAABAI'],
        to='+19498285996'
    )

print(message.sid)