import itertools

weights = [1, 3, 5, 4]
k = 3
res = []
def comb(lst, idx):
    if idx == 4:
        return
    res.append([lst[:idx], lst[idx:]])
    print(res)
    return comb(lst[idx:], 0)

print(list(itertools.combinations(weights, 3)))


#[[1],[3],[5,1]]
#[[1],[3,5],[1]]
#[[1,3],[5],[1]]

# def split_recursive(arr, k):
#     if k == 1:
#         return [[arr]]
#     if len(arr) < k:
#         return []
#
#     result = []
#     # Первый подсписок может быть любой длины от 1 до (n - k + 1)
#     for i in range(1, len(arr) - k + 2):
#         first_part = [arr[:i]]
#         for rest_parts in split_recursive(arr[i:], k - 1):
#             result.append(first_part + rest_parts)
#     return result
#
#
# arr = [1, 2, 3, 4]
# k = 3
# for partition in split_recursive(arr, k):
#     print(partition)


