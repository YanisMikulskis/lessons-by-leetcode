class Solution:
    '''
    Вам дан целочисленный массив ranks, представляющий ранги некоторых механиков. ranks[i] — это ранг i-го механика.
    Механик с рангом r может починить n машин за r * n² минут.
    Также вам дано целое число cars, представляющее общее количество машин, ожидающих ремонта в гараже.
    Необходимо вернуть минимальное время, за которое можно починить все машины.
    Примечание: Все механики могут работать одновременно.
    Example 1:

    Input: ranks = [4,2,3,1], cars = 10
    Output: 16
    Explanation:
    - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
    - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
    - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
    - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
    It can be proved that the cars cannot be repaired in less than 16 minutes.
    '''
    def repairCars(self, ranks: list[int], cars: int) -> int:

        max_time = 0 # сначала найдем вообще максимальное время, за которое механики сделают машины
        min_time = 0
        max_time = []
        for i in ranks:
            if i == max(ranks):
                cars_for_max = cars - (len(ranks) - 1)
                print(cars_for_max)
                max_time.append(i * cars_for_max * cars_for_max)
            else:
                max_time.append(i * 1 * 1)




        max_time = max(max_time)



        # times = list(range(max_time + 1))
        # left = 0
        # right = max_time
        # while left < right:
        #     mid = (left + right) // 2


sol = Solution()
sol.repairCars(ranks = [4,2,3,1], cars = 10)












print(min(2,4))


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        min_rank, max_rank = ranks[0], ranks[0]

        # Find min and max rank dynamically
        for rank in ranks:
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)

        # Frequency list to count mechanics with each rank
        freq = [0] * (max_rank + 1)
        for rank in ranks:
            min_rank = min(min_rank, rank)
            freq[rank] += 1

        # Minimum possible time, Maximum possible time
        low = 1
        high = min_rank * cars * cars

        # Perform binary search to find the minimum time required
        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0

            # Calculate the total number of cars that can be repaired in 'mid' time
            for rank in range(1, max_rank + 1):
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))

            # Adjust the search boundaries based on the number of cars repaired
            if cars_repaired >= cars:
                high = mid  # Try to find a smaller time
            else:
                low = mid + 1  # Need more time

        return low