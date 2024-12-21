import datetime, re


def get_dates_to_call_for_year(year, month, day):
    """
    takes a year, month, and day, and returns a list of dates, 7 before and 7 after, for that year, accounting for leap year and next/last year
    :param year:
    :param month:
    :param day:
    :return:
    """
    base = datetime.date(year, month, day)
    date_list = [base - datetime.timedelta(days=x+1) for x in range(-8,7)]
    date_list_pretty = []
    for i in date_list:
        date_list_pretty.append(str(i))
    return date_list_pretty


def generate_master_date_list(month, day):
    """
    takes a month and a day and generates a list of days,
    7 before and 7 after, for every year back to 1950
    :param month:
    :param day:
    :return: list of dates
    """
    current_year = str(datetime.datetime.today())
    year_only = int(re.findall(r"(\d{,4})-.+", current_year)[0])
    #do we want to use 1950? may need to look at request limits.
    #we might be fine with the past 25 years
    year_set = range(year_only, 1950, -1)
    master_date_list = []
    for year in year_set:
        single_year_dates = get_dates_to_call_for_year(year, month, day)
        master_date_list.append(single_year_dates)
    return master_date_list

if __name__ == '__main__':
    print(generate_master_date_list(6, 23))