import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
three_years_ago = today - relativedelta(years=3)
one_and_half_year_ago = today - relativedelta(years=1, months=6)
one_year_ago = today - relativedelta(years=1)
ninety_days_ago = today - relativedelta(days=90)


# На вход функции подаётся дата приёма сотрудника на работу и брал ли он больничный(True или False).
# На выходе получаем премию в процентном выражении от зарплаты.
# Длительность работы сотрудника считается относительно сегодняшней даты (даты запуска функции).

def premium_calculation(hire_date, sick_last_year):
    premium_percent = 0
    # Проверка правильности введённых пользователем значений
    try:
        hire_date_obj = datetime.datetime.strptime(hire_date, "%Y-%m-%d").date()
    except Exception as e:
        print(f"Unable to parse date: {e}")
        raise
    if not isinstance(sick_last_year, bool):
        msg = f"{sick_last_year} must be True or False"
        return msg

    # Расчёт базовой премии, в зависимости от кол-ва отработанных лет.
    if hire_date_obj > ninety_days_ago:
        # менее 90 дней
        premium_percent = 0
    elif one_and_half_year_ago < hire_date_obj <= ninety_days_ago:
        # от 90 дней до 1,5 лет
        premium_percent = 15
    elif three_years_ago <= hire_date_obj <= one_and_half_year_ago:
        # от 1,5 лет до 3-х лет включительно
        premium_percent = 25
    elif three_years_ago > hire_date_obj:
        # больше 3-х лет
        premium_percent = 30
    else:
        print("I can't count the premium")

    # Прибавка, если не брал больничный и работает не меньше года.
    if sick_last_year is False and hire_date_obj <= one_year_ago:
        premium_percent += 3

    return premium_percent
