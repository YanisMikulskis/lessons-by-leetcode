class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:


        bot = {
        }

        for allow in allowed:
            if allow[:2] not in bot:
                bot[allow[:2]] = []
            bot[allow[:2]].append(allow[-1])
        print(bot)

        basics = [f'{bottom[i]}{bottom[i + 1]}' for i in range(len(bottom) - 1)]
        print(basics)
        couples_basics = []
        for base in basics:
            try:
                couples_basics.append(bot[base])
            except KeyError:
                return False

        print(couples_basics)

        top = []
        for _ in range(len(couples_basics) - 1):
            for item in couples_basics[_]:
                for elem in couples_basics[_ + 1]:
                    top.append(f'{item}{elem}')
        print(top)

        print(F'0000')
        array = [
            ['A', 'B'],['C'],['D', 'E']
        ]
        print(f'----')
        array2 = [['a', 'b'],['c'], ['d', 'e']]
        temp = []
        i = 0

        while i < len(array2) - 1:

            for j in range(len(array2[i])):
                temp.append(array2[i][j])
                for item in range(i + 1, len(array2)):
                    for elem in array2[item]:
                        temp[-1] += elem



            print(temp)
            i += 1























sol = Solution()
sol.pyramidTransition(bottom = "ABC", allowed = ["ABD", "BCE", "BCF"])
# sol.pyramidTransition(bottom='ABCDE', allowed=None)