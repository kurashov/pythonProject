cur = int(input())
best_sum = cur
sum = 0
while cur != 0:
    sum += cur
    if best_sum < sum:
        best_sum = sum
    elif sum < 0:
        sum = 0
    cur = int(input())

print(best_sum)
