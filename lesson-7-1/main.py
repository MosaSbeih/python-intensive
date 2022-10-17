import calendar

from decorators import short_form, translate


@translate(language="German")
@short_form
def get_data():
    return calendar.day_name


if __name__ == '__main__':
    print(get_data())
