class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        all_strings = 3 * (2 ** (n - 1))
        test = ['a', 'b', 'c', 'd']



        def factorial(n):

            if n == 1:
                return n
            return n * factorial(n-1)
        print(factorial(10))
        # arr = ['a', 'a', 'a', 'a', 'a']
        # col = 2
        # for i in range(len(arr)):

        def func(idx, temp):
            temp = [test[idx] for _ in range(factorial(len(test) - 1))]
            cnt = len(temp) // (len(test) - 1)
            temp_slice = list(''.join(list(map(lambda x: x * cnt, [let for let in test if let != test[idx]]))))
            print(f'temp = {temp}')
            print(f'temp-slice = {temp_slice}')
            print(f'zip = {list(map(lambda x: ''.join(x), zip(temp, temp_slice)))}')






        func(0, [])


        # func(0, [])

sol = Solution()
sol.getHappyString(3, 9)
#
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)





print(factorial(10))























