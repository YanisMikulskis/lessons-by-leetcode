class Solution:
    '''
    Условие задачи

    В лесу живёт неизвестное количество кроликов. Мы спросили у n кроликов:
    "Сколько кроликов такого же цвета, как вы?" и собрали ответы в массив answers, где answers[i] -
    это ответ i-го кролика.

    По данному массиву answers нужно вернуть минимально возможное количество кроликов в лесу.

    Примеры

    Пример 1:

    Входные данные:
    answers = [1,1,2]

    Выходные данные:
    5

    Объяснение:

    Два кролика, ответившие "1", могут быть одного цвета (например, красные)
    Кролик, ответивший "2", не может быть красным (иначе было бы несоответствие)
    Пусть кролик, ответивший "2", будет синим
    Тогда должно быть ещё 2 синих кролика, которые не дали ответа
    1 1
    2 2 2
    3 3 3 3
    4 4 4 4 4    4 4 4 4 4    4 4 4 4 4    4 4 4 4 4
    '''
    def numRabbits(self, answers: list[int]) -> int:
        if not answers:
            return 0
        groups = {
        }
        for i in answers:
            if i not in groups:
                groups.setdefault(i, [])
            groups[i].append(i)

        all_rabbits = 0
        for rabbits in list(groups.values()):
            all_rabbits += len(rabbits)
            remainder = len(rabbits) % (rabbits[0] + 1)
            if remainder:
                all_rabbits += ((rabbits[0] + 1) - remainder)

        return all_rabbits




sol = Solution()
sol.numRabbits([2, 2, 2, 2, 2])
sol.numRabbits([0,1,0, 1])
sol.numRabbits(answers = [1, 1, 2])
sol.numRabbits(answers = [3, 3, 3, 3, 2, 2, 2, 1, 1, 0, 0])
sol.numRabbits([10,10,10])