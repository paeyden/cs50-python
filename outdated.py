def outdated():
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    while True:
        try:
            user_input = input("Date: ").strip()

            # Case 1: Format MM/DD/YYYY
            if "/" in user_input:
                month, day, year = user_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if month > 12 or day > 31:
                    raise ValueError

                print(f"{year}-{month:02}-{day:02}")
                break

            # Case 2: Format Month DD, YYYY
            elif "," in user_input:
                month_day, year = user_input.split(",")
                month_name, day = month_day.strip().split()
                day = int(day)
                year = int(year.strip())
                month = months[month_name]

                print(f"{year}-{month}-{day:02}")
                break

        except (ValueError, KeyError):
            continue

outdated()
