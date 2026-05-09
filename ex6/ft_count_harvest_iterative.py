def ft_count_harvest_iterative():
    days = input("Days until harvest: ")
    limits = range(1, int(days) + 1)
    for nb in limits:
        print(f"Day {nb}")
    print("Harvest time!")
