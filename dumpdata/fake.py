import random
import string

from Citigo_Ex1.dumpdata import Database

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
        user = (name,mail)
        listUser.append(user)
    db.insert_to("dim_users",listUser)

def insert_product():
    listProduct = []
    for i in range(1, 101):
        product = ("Product " +str(i),)
        listProduct.append(product)
    db.insert_to("dim_product", listProduct)

def insert_retailer():
    listRetailer = []
    for i in range(1, 101):
        retailer = ("Kiot "+str(i),)
        listRetailer.append(retailer)
    db.insert_to("dim_retailer",listRetailer)

def insert_day():
    listDay = []
    for i in range(1,32):
        _day = (i, i)
        listDay.append(_day)
    db.insert_to("dim_day",listDay)
def insert_week():
    listWeek = []
    for i in range(1,5):
        _week = (i,i)
        listWeek.append(_week)
    db.insert_to("dim_week",listWeek)
def insert_quater():
    listQuater = []
    for i in range(1, 5):
        _quater = (i, i)
        listQuater.append(_quater)
    db.insert_to("dim_quater",listQuater)
def insert_month():
    list_month = []
    for i in range(1,13):
        list_month.append((i,i))
    db.insert_to("dim_month",list_month)
def insert_year():
    list_year = []
    for i in range(2000, 2101):
        list_year.append((i,i))
    db.insert_to("dim_years",list_year)

def get_quater_id():
    print()


# input: dd/mm/yyyy
# output: dayid, weekid, monthid, quaterid, yearid
def get_date():
    listDate = []
    months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    for _year in range(2019,2021):
        year_id = _year
        day_id = 0
        week_id = 0
        month_id = 0
        quater_id = 0
        for _month in range(1,13):
            d = 0
            w = 1
            if _month == 1: d = 6
            for _day in range(1,months[_month]+1):
                day_id = _day
                d += 1
                week_id = w

                if _day > 25 :
                    d += 1
                    week_id = 1
                    month_id = _month + 1


                if _month == 12:
                    month_id = 1
                    quater_id = 1

                if d == 7:
                    d = 0
                    w += 1




if __name__ == "__main__":
    print()
    get_date();


