def is_leap(years):
    leap = False

    if (years % 4) == 0:
        if (years % 100) or (years % 400) == 0:
            return True
        else:
            return False
    else:
        return False


year = int(input())
print(is_leap(year))

# year_string = str(years)
#    length = len(year_string)
#    new_year = int(year_string[length - 2:])
#    if (new_year % 4) == 0:
#       leap = True
#       return leap
