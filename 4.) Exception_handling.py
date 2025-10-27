while True:
    a = int(input())
    b = int(input())

    try:
        res = a + b

    except ZeroDivisionError:
        print("pls dont give 0 to denominator")
        continue

    else:
        print(res)

    finally:
        print("my code is running well")
