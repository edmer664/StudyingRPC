from pypresence import Presence
import time
from itertools import cycle
import requests
import os

client_id = "902536560539484202"

start_time = time.time()

RPC = Presence(client_id=client_id)
RPC.connect()

lines = [
    "PLEASE DO NOT",
    "DISTURB, THANKS!",
]
r = requests.get("https://type.fit/api/quotes")
response = r.json()


while 1:
    for q in response:
        os.system("cls")
        print("MOTIVATE YOUR SELF \n\n\n")
        print(f'''"{q["text"]}"''',"\n -",q["author"])
        for i in lines:
            RPC.update(small_image="book",large_image="book", details="I'm studying",
                state=i,
                start=start_time)
            time.sleep(2) 