class Solution:
    def maxDiff(self, num: int) -> int:
        num_max = num_min = list(str(num))

        def mutate_number(target, new_number, arr):

            return list(map(lambda x:new_number if x == target else x, arr))

        for i in range(len(num_max)):
            if num_max[i] != '9':
                num_max = mutate_number(num_max[i], '9', num_max)
                break

        for i in range(len(num_min)):
            target = num_min[i]
            if i == 0:
                if target != '1':
                    num_min = mutate_number(target, '1', num_min)
                    break
            else:
                if num_min[0] != target and target != '0':
                    num_min = mutate_number(target, '0', num_min)
                    break

        return int(''.join(num_max)) - int(''.join(num_min))