def readable_timedelta(days):
    # insert your docstring here
''' The function readable_timedelta takes the input of an integer in days
    and gives an output containing the weeks and days'''

    weeks = days // 7
    remainder = days % 7
    return ("{} week(s) and {} day(s)".format(weeks, remainder))
