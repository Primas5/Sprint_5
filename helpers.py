import random
import string

def generate_random_email():
    username_length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    
    domains = ["ya.ru","gmail.com", "yahoo.com", "outlook.com", "example.ru", "test.net"]
    domain = random.choice(domains)
    
    email = f"{username}@{domain}"
    return email

def generate_bad_email():
    username_length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return username
