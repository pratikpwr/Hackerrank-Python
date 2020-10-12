n = int(input())

i = 0
lst = list()
while i < n:
    # print(n - i - 1)
    lst.append(n - i - 1)
    i = i + 1

new_lst = sorted(lst)
# print(new_lst)

for l in new_lst:
    print(new_lst[l] * new_lst[l])
