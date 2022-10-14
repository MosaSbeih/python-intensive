import calendar
import locale
from functools import wraps


def short_form(func):
    @wraps(func)
    def wrapper():
        return list(calendar.day_abbr)

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
