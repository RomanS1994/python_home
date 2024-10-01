#### --------- Тема 3. Модулі datetime та time. Робота з випадковими величинами

import datetime

# now = datetime.datetime.now()
# print(now)


# from datetime import datetime
#
# print(datetime.now().day)

#
from datetime import datetime, timedelta
from re import match

# from black import datetime, timezone

#
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)
#
#
# print(seventh_day_2020)  # 2020-02-04 14:00:00
# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(four_weeks_interval)  # 2019-12-10 14:00:00


######## Отримання дати
# print(datetime.now())

# minus_one_year = datetime(year=2024, day= 3, month=9)
# my_date = datetime(year=2025, day=4, month= 9)
# my_year = my_date - minus_one_year
# print(my_year.days)
# now1 = datetime.now()
# print(now1)
# now = datetime.now(timezone.utc)
# print(now)
# iso_calendar = now.isocalendar()
# print(iso_calendar)

# from datetime import datetime, timezone, timedelta
#
# # Час у конкретній часовій зоні
# timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
# timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
#
# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)
# print(timezone_datetime)
#
# import time
# from time import ctime
#
# current_time = time.time()
# print(ctime(current_time))
# print("start")
# time.sleep(19)
# print('End')

#####------------ Рандом
# from random import random
# number =  random() * 1000
# print(f"{number:.0f}")

##### -------- Модуль MATH
# import math
# test = math.tau
# print(test)
