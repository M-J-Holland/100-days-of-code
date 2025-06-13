# Code challenge using lists and the random module

import random

friends = ['mathew', 'jim', 'tom', 'sam', 'beth', 'sandy',]

paying_friend_index = random.randint(0, len(friends))
person_to_pay = friends[paying_friend_index]

print(f"The person that will be paying the bill will be: {person_to_pay.title()}")