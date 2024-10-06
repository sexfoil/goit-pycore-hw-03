import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min < 1 or max > 1000 or quantity < min or quantity > max:
            raise ValueError("Invalid value(s) in arguments.")
        
        num_set = set()
        while len(num_set) < quantity:
            num_set.add(random.randint(min, max))

        numbers = list(num_set)       
        return sorted(numbers)
    
    except ValueError as e:
        print(e)

    return []


min_number = int(input("Enter min number value (MIN => 1) >>> "))
max_number = int(input("Enter max number value (MAX <= 1000) >>> "))
numbers_amount = int(input("Enter amount of numbers (MIN <= amount <= MAX) >>> "))

lottery_numbers = get_numbers_ticket(min_number, max_number, numbers_amount)
print(f"Your numbers are: {lottery_numbers}")
