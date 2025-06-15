class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        prefix = [0]
        for i in range(len(differences)):
            prefix.append(prefix[-1] + differences[i])
        first_el, temp = lower - prefix[0], 0
        while upper - first_el >= 0:
            temp = temp + 1 if all(lower <= first_el + i <= upper for i in prefix) else temp
            first_el += 1

            def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
                x = y = cur = 0
                for d in differences:
                    cur += d
                    x = min(x, cur)
                    y = max(y, cur)
                    if y - x > upper - lower:
                        return 0
                return (upper - lower) - (y - x) + 1

            # [i for i in prefix]
            # for i in prefix:
            #     if lower <= first_el + i <= upper:
            #         continue
            #     else:
            #         stopped = 1
            #         break
            # first_el += 1
            # if stopped:
            #     continue
            # temp += 1





            # res, stopped = [], False
            # for i in prefix:
            #     if lower <= first_el + i <= upper:
            #         continue
            #         # res.append(first_el + i)
            #     else:
            #         stopped = True
            #         break
            # first_el += 1
            # if stopped:
            #     print(f'ff')
            #     continue
            # all_res.append(res)
            # temp += 1



        print(temp)











sol = Solution()
# sol.numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6)
# sol.numberOfArrays([3, -4, 2], -10,-5)
sol.numberOfArrays(differences = [1, -3, 4],lower = 1,upper = 6)
# sol.numberOfArrays(differences = [5, -3, -1],
# lower = -4,
# upper = 5)