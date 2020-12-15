phone_numbers = {}
phone_numbers["Jenny"] = "(555) 867-5309"

print(phone_numbers["Jenny"])



capitals = {}
capitals["Idaho"] = "Boise"
capitals["Utah"] = "Salt Lake City"
capitals["California"] = "Sacramento"
# ... other states here ...

state = input("Enter a state name: ")
capital = capitals[state]

print("The capital of {} is {}".format(state, capital))