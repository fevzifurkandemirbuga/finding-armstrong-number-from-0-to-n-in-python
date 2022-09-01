input = int(input("enter a number: "))
for i in range(1, input+1):
    num = i
    sum = 0
    while num > 0:
        digit = num % 10
        num = num//10
        sum += digit**3
    if i == sum:
        print(i)
