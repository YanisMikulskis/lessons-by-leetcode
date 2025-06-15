# разделить на пары с одинаковыми числами элементы списка и вернуть true если это возможно иначе false
from collections import Counter

def function(nums):
    count_numbers = Counter(nums)
    for number in count_numbers.values():
        if number % 2 != 0:
            return False
    return True

print(function(nums= [3,2,3,2,2,2]))

print(function(nums=[1,1,2,2,3,4]))