# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    86. Разделение связного списка
    Условие:

    Дан односвязный список head и целое число x.
    Нужно переставить узлы списка так, чтобы:

    Все узлы со значением меньше x находились до узлов, больших или равных x.
    Порядок элементов должен сохраниться.
    Верните новую голову измененного списка.

    Пример 1:

    Вход: head = [1,4,3,2,5,2], x = 3
    Выход: [1,2,2,4,3,5]
    Объяснение:
    Узлы [1,2,2] (меньше 3) идут первыми.
    Узлы [4,3,5] (больше или равны 3) идут следом.
    Порядок внутри групп сохранен.
    '''
    def partition(self, head, x=3):
        left_lst, right_lst = ListNode(0), ListNode(0)
        left, right = left_lst, right_lst

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = right_lst.next
        right.next = None

        return left_lst.next


list_node = []





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#

new_head = []

def make_head(head): # новая функция создания связного списка
    head_list = ListNode(head[0])
    core = head_list

    for val in head[1:]:
        core.next = ListNode(val)
        core = core.next

    return head_list

result = make_head([1,4,3,2,5,2])
# while result:
#     print(result.val)
#     result = result.next








#
sol = Solution()
print(sol.partition(result))