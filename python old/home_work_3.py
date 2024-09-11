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
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         spaces_to_add = (length - len(string)) // 2
#         formatted_string = ' ' * spaces_to_add + string
#         return formatted_string

# # Приклади використання функції для тестів
# print(format_string('aaaaaaaaaaaaaaaaac', 12))
# print(format_string('abaa', 15))

#----------- Практика 7 ---------------------
# def make_article(title, *topics):
#     print(topics)


# make_article("Title", "first", "second", "third")  # ('first', 'second', 'third')


# def make_article(title, **comments):
#     print(comments)


# make_article("Title", comment_one="first", comment_two="second", comment_third="third")
# # {'comment_one': 'first', 'comment_two': 'second', 'comment_third': 'third'}

#----------- number 7 ---------------------
# def first(size, *result_first):
#     return len(result_first)
    


# def second(size, **result_second):
#     return len(result_second)

# print(first(5, "first", "second", "third"))
# print(first(1, "Alex", "Boris"))
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))\


def cost_delivery(*quantity, discount = 0):
    if quantity[0] > 0 and discount > 0:
        return ((quantity[0] - 1) * 2 + 5) * discount 
    else:
        return ((quantity[0] - 1) * 2 + 5)
print(cost_delivery(2, 1, 2, 3, discount=0.5))

def cost_delivery(quantity, *_, discount=0):
    
    """Функція повертає суму за доставлення замовлення.

     Перший параметр quantity; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
    
    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result