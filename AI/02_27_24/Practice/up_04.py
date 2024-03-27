# Функция - приема списък от числа, премахва всички съседни повтарящи се елементи.
# def remove_adjacent(nums):
# remove_adjacent([1, 2, 2, 3]) # [1, 2, 3]
# remove_adjacent([2, 2, 3, 3, 3]) # [2, 3]

def remove_adjacent(nums):
    result = []
    for num in nums:
        if not result or num != result[-1]:
            result.append(num)
    return result

result1 = remove_adjacent([1, 2, 2, 3])
result2 = remove_adjacent([2, 2, 3, 3, 3])

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
    