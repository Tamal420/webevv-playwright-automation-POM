import random
import string

def get_human_first_name():
    first_names = ["John", "Jane", "Michael", "Sarah", "Robert", "Emily", "David", "Olivia", "James", "Sophia"]
    return random.choice(first_names)

def get_human_last_name():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    return random.choice(last_names)

def get_human_username():
    names = ["jason", "sarah", "mike", "emily", "robert", "sophia", "david", "lisa"]
    random_num = random.randint(10, 99) #2 digits number generator for username uniqueness
    return f"{random.choice(names)}{random_num}"

def get_random_digits(length):
    #Random length character string generator for digits only
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(length))
