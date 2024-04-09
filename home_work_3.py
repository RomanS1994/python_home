# base_rate = 40
# price_per_km = 10
# total_trip = 0

# def calculate_trip_price(distance_km):
#     global total_trip  
#     total_trip += 1
#     return base_rate + distance_km * price_per_km

# print(calculate_trip_price(10))
# print("Total trips:", total_trip)

#----------- Number 6---------------------
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces_to_add = (length - len(string)) // 2
        formatted_string = ' ' * spaces_to_add + string
        return formatted_string

# Приклади використання функції для тестів
print(format_string('aaaaaaaaaaaaaaaaac', 12))
print(format_string('abaa', 15))