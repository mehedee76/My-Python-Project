for year in range(2017,2100):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year)
        else:
            print(year)
