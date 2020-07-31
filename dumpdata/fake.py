import Database
import random
import string
db = Database.DataBase()

def random_int(start, end):
    return random.randint(start,end)

def random_string(start,end):
    length = random.randint(start,end)
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def insert_users():
    listUser = []
    for i in range(1, 101):
        name = random_string(10,15)
        mail = name + "@gmail.com"
        






if __name__ == "__main__":
    print()
    insert_users()

