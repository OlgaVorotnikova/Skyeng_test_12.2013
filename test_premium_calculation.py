import pytest
from datetime import date
from premium_calculation import premium_calculation
from dateutil.relativedelta import relativedelta

today = date.today()
today_plus_1d = today + relativedelta(days=1)
today_min_1d = today - relativedelta(days=1)
today_plus_100y = today + relativedelta(years=100)
three_years_ago = today - relativedelta(years=3)
three_years_ago_min_1d = three_years_ago - relativedelta(days=1)
three_years_ago_plus_1d = three_years_ago + relativedelta(days=1)
one_and_half_year_ago = today - relativedelta(years=1, months=6)
one_and_half_year_ago_min_1d = one_and_half_year_ago - relativedelta(days=1)
one_and_half_year_ago_plus_1d = one_and_half_year_ago + relativedelta(days=1)
one_year_ago = today - relativedelta(years=1)
one_year_ago_min_1d = one_year_ago - relativedelta(days=1)
one_year_ago_plus_1d = one_year_ago + relativedelta(days=1)
ninety_days_ago = today - relativedelta(days=90)
ninety_days_ago_min_1d = ninety_days_ago - relativedelta(days=1)
ninety_days_ago_plus_1d = ninety_days_ago + relativedelta(days=1)
fifty_years_ago = today - relativedelta(years=50)


# print(f"today:{today}")
# print(f"today_min_1d:{today_min_1d}")
# print(f"today_plus_1d:{today_plus_1d}")
# print(f"ninety_days_ago_plus_1d:{ninety_days_ago_plus_1d}")
# print(f"ninety_days_ago_min_1d:{ninety_days_ago_min_1d}")
# print(f"ninety_days_ago:{ninety_days_ago}")
# print(f"one_year_ago_plus_1d:{one_year_ago_plus_1d}")
# print(f"one_year_ago_min_1d:{one_year_ago_min_1d}")
# print(f"one_year_ago:{one_year_ago}")
# print(f"one_and_half_year_ago_plus_1d:{one_and_half_year_ago_plus_1d}")
# print(f"one_and_half_year_ago_min_1d:{one_and_half_year_ago_min_1d}")
# print(f"one_and_half_year_ago:{one_and_half_year_ago}")
# print(f"three_years_ago_plus_1d:{three_years_ago_plus_1d}")
# print(f"three_years_ago_min_1d:{three_years_ago_min_1d}")
# print(f"three_years_ago:{three_years_ago}")
# print(f"fifty_years_ago:{fifty_years_ago}")
# print(f"today_plus_100y:{today_plus_100y}")

@pytest.mark.positive_tests
class TestPositiveTests():
    @pytest.mark.parametrize("hire_date", [three_years_ago_min_1d, fifty_years_ago])
    def test_premium_33_percent(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        print(type(hire_date_str))
        assert premium_calculation(hire_date_str, False) == 33

    @pytest.mark.parametrize("hire_date", [three_years_ago_min_1d, fifty_years_ago])
    def test_premium_30_percent(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        #   print(type(hire_date_str))
        assert premium_calculation(hire_date_str, True) == 30

    @pytest.mark.parametrize("hire_date",
                             [three_years_ago, three_years_ago_plus_1d, one_and_half_year_ago_min_1d,
                              one_and_half_year_ago])
    def test_premium_28_percent(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        assert premium_calculation(hire_date_str, False) == 28

    @pytest.mark.parametrize("hire_date",
                             [three_years_ago, three_years_ago_plus_1d, one_and_half_year_ago,
                              one_and_half_year_ago_min_1d])
    def test_premium_25_percent(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        assert premium_calculation(hire_date_str, True) == 25

    @pytest.mark.parametrize("hire_date", [one_year_ago_min_1d, one_year_ago, one_and_half_year_ago_plus_1d])
    def test_premium_18_percent(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        assert premium_calculation(hire_date_str, False) == 18

    @pytest.mark.parametrize("hire_date", [one_year_ago_min_1d, one_year_ago, one_and_half_year_ago_plus_1d])
    def test_premium_15_percent_more_than_a_year(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        assert premium_calculation(hire_date_str, True) == 15

    @pytest.mark.parametrize("hire_date", [one_year_ago_plus_1d, ninety_days_ago, ninety_days_ago_min_1d])
    def test_premium_15_percent_less_than_a_year(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        assert premium_calculation(hire_date_str, True) == 15

    @pytest.mark.parametrize("hire_date", [ninety_days_ago_plus_1d, today_min_1d, today])
    def test_premium_0_percent(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        assert premium_calculation(hire_date_str, True) == 0


@pytest.mark.negative_tests
class TestNegativeTests:
    @pytest.mark.parametrize("hire_date", [today_plus_1d, today_plus_100y])
    def test_premium_0_percent_future(self, hire_date):
        hire_date_str = str(hire_date)
        print(hire_date_str)
        assert premium_calculation(hire_date_str, True) == 0

    @pytest.mark.parametrize("hire_date", ['0', 'abc', '-1'])
    def test_not_valid_date(self, hire_date):
        with pytest.raises(Exception):
            premium_calculation(hire_date, True)

    @pytest.mark.parametrize("sick_last_year", ['TTT', '2023-12-24'])
    def test_not_valid_sick_last_year(self, sick_last_year):
        msg = premium_calculation('2023-12-24', sick_last_year)
        print(msg)
        assert 'must be True or False' in msg
