import random
from datetime import datetime

lucky_Number = random.randint(1, 100)

today = datetime.today()
day = today.strftime("%B %d, %Y")

print(f"Today is {day} and your lucky number is: {lucky_Number}")
