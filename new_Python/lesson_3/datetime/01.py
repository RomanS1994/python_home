import datetime

from datetime import datetime, date


def get_days_from_today(dats):
    """
    Calculates the difference between two dates

    Parameters:
    date (str).

    Returns:
    result.days(int)
    """
    try:
        datetime_obj = datetime.strptime(dats, "%Y-%m-%d").date()
        print(datetime_obj)
        date_now = date.today()
        print(date_now)

        result = (date_now - datetime_obj).days
        print(result)
        return result
    except:
        return "Enter the correct format"


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2021-10"))
