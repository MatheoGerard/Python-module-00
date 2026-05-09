def ft_water_reminder():
    last_water_day = input("Days since last watering: ")
    if int(last_water_day) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
