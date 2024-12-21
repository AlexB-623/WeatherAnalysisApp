import dates_to_call, gps_coords_to_call

while True:
    while True:
        test_location = input("What location would you like to get a weather analysis for?"
                              "(enter: city, state)")
        location = gps_coords_to_call.convert_location_to_gps(test_location)
        if type(location) == tuple:
            break
        else:
            print(location)

    while True:
        test_month = input("What month are you interested in? (enter month number 01-12)")
        try:
            month = int(test_month)
        except ValueError:
            print("Please enter a number 1-12")
            continue
        if month >= 1 and month <= 12:
            break
        else:
            print("Please enter a number 1-12")

    while True:
        test_day = input(f"What day of {test_month} are you interested in?")
        try:
            day = int(test_day)
        except ValueError:
            print("Please enter a number 1-31")
            continue
        if day >= 1 and day <= 31:
            break
        else:
            print("Please enter a number 1-31")

    date_list = dates_to_call.generate_master_date_list(month, day)
    #print(date_list)
