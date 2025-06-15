from collections import Counter
def function(nums, queries):
    k = 0
    def check_zero(lst):
        if Counter(lst)[0] == len(lst):
            return True
        return False

    if check_zero(nums):
        return k


    def mutate(left, right, val):
        for el in range(left, right + 1):
            nums[el] -= val
            if nums[el] < 0:
                return -1
        if check_zero(nums):
            return 1


    for q in queries:
        result_mutate = mutate(q[0], q[1], q[2])
        k += 1
        if result_mutate == 1:
            return f'k = {k}'
        elif result_mutate == -1:
            return -1
    return -1








print(function([1,2,3], [[0,1,1], [1,2,2]]))
print(f'--------------')
print(function([5,3,7], [[0,2,3], [1,2,2], [0,0,2]]))
print(f'--------------')
print(function([3,4,2,5], [[0,2,2], [1,3,3], [0,3,1]]))
print(f'--------------')
print(function([0,0,0,0], [[0,2,2], [1,3,3], [0,3,1]]))
print(f'--------------')

print(function([10,5,0,7,3], [[0,4,3], [1,3,2]]))
print(function([5,5,5], [[0,2,2], [0,2,3]]))