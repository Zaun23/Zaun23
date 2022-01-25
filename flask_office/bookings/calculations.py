# FILE USED FOR CALCULATING PRICE FOR ROOMS
from datetime import datetime

# defining price list and dictionary of rooms
# 0 in price list is a placeholder, since index starts at 0
# but our list starts at 1 for simplicity
room_price_list = [0, 10, 10, 10, 25, 45, 90]
room_list = {
    "Ristretto" : 1,
    "Espresso" : 2,
    "Macchiato": 3,
    "Cappuccino": 4,
    "Lungo": 5,
    "Schlossbergblick": 6 
}


def convertTimeDuration(start_time_obj, end_time_obj):
    t1 = start_time_obj.strftime("%H:%M:%S")
    t2 = end_time_obj.strftime("%H:%M:%S")
    start = datetime.strptime(t1, "%H:%M:%S")
    end = datetime.strptime(t2, "%H:%M:%S")
    t = (end - start)    
    return (t.total_seconds() / 3600)


# function to calculate the price of the room
# returns the the price
def calculateRoomPrice(room_string, booked_hours):
    temp_cost = float(booked_hours) * room_price_list[room_list[room_string]]
    half_percentage = 0.8
    full_percentage = 0.675

    if(int(room_list[room_string]) > 3):
        if(float(booked_hours) > 3 and float(booked_hours) < 8):
            temp_cost *= half_percentage
        elif(float(booked_hours) > 7):
            temp_cost *= full_percentage

    return temp_cost
