def is_leap(year):
    leap = False

    while 1900<= year <= 10**5:
        if int(year) % 4 == 0:
            if int(year) % 100 ==0:
                if int(year) % 400 ==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

year = int(input())
print(is_leap(year))
