from pypresence import Presence
import time
from itertools import cycle

client_id = "902536560539484202"

start_time = time.time()

RPC = Presence(client_id=client_id)
RPC.connect()

lines = [
    "Please do not",
    "Disturb me while",
    "Studying, Thank you",
]
            
while 1:
    for i in cycle(lines):
        RPC.update(large_image="book", details="I'm studying",
            state=i,
            start=start_time)
        time.sleep(3) 