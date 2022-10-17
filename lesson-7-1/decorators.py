import calendar
import locale
from functools import wraps


def abbr_data() -> dict:
    data_dict = {}
    weekday_data = list(calendar.day_name)
    abbr_weekday_date = list(calendar.day_abbr)

    for index in range(len(weekday_data)):
        data_dict[weekday_data[index]] = abbr_weekday_date[index]

    return data_dict


def short_form(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = abbr_data()
        abbr_weekday_list = []
        weekdays_list = list(func(*args, **kwargs))

        for day in weekdays_list:
            abbr_weekday_list.append(data[day])

        return abbr_weekday_list

    return wrapper


def translate(language: str = "English"):
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            locale.setlocale(locale.LC_ALL, language)

            translated = list(func(*args, **kwargs))

            locale.setlocale(locale.LC_ALL, "English")

            return translated

        return wrapper

    return inner_function
