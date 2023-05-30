def divisible_by_three(arr=list):
    return [x for x in arr if x % 3 == 0]

test = [1, 12, 4, 15, 3, 6, 123]
print(divisible_by_three(test))