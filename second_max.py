cur = second_max = max = int(input())
while cur != 0:
    if cur > max:
        second_max = max
        max = cur
    elif cur > second_max:
        second_max = cur
    elif max == second_max:
        second_max = cur
    cur = int(input())

print(second_max if second_max != max else "NO")
