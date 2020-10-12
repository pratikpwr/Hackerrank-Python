inp = input()
num = 0
try:
    num = int(inp)
except:
    print("Enter valid Number.")


def is_odd(n):
    if (n % 2) == 0:
        return False
    else:
        return True


odd = is_odd(num)

if odd or 6 <= num <= 20:
    print("Weird")
elif not odd or 2 <= num <= 5 or num < 20:
    print("Not Weird")
