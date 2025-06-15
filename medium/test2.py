from collections import Counter
def func(words, groups):
    zip_list = list(zip(words, groups))
    start_len, max_len = 1, len(max(words, key=lambda x: len(x)))
    final_list = []


    #--------------

    def check_hemming(let1, let2):
        if len([s for s in list(map(lambda x: set(x), zip(let1, let2))) if len(s) == 2]) == 1:
            return True
        return False




    # --------------





    while start_len <= max_len:
        temp_list = [i for i in zip_list if len(i[0]) == start_len]
        print(temp_list)

        tmp_res = []
        for let in range(len(temp_list)):
            group = temp_list[let][1] # start_len
            tmp = [temp_list[let]]

            for next_let in range(let + 1, len(temp_list)):
                if temp_list[next_let][1] != group:

                    group = temp_list[next_let][1]
                    tmp.append(temp_list[next_let])
            print(f'tmp = {tmp}')


            if len(tmp) > len(tmp_res):
                tmp_res = tmp

        print(f'tmp_tes = {tmp_res}')


        # temp_dict = {
        #
        # }
        #
        # for i in temp_list:
        #     if i[1] not in temp_dict:
        #         temp_dict.setdefault(i[1], [])
        #     temp_dict[i[1]].append(i[0])
        # print(temp_dict)
        #
        #
        # tmp_res = []

        start_len += 1






        # print(f'check = {max(temp_list, key=lambda x:x[1])}')
        #
        # print(temp_list)
        # start_len += 1
    print(f'max_len = {max_len}')

# print(func(words = ["abc", "acc", "adc", "bcc"],groups = [0, 1, 0, 1]))
# print()
print(func(words=["a", "b", "ab", "aa", "bb"], groups=[0, 1, 0, 1, 0]))
# # groups = [0, 1, 0, 1, 0]))
# # print(func(words = ["bab","dab","cab"], groups = [1,2,2]))
# # print(func(words = ["bab","dabfdsfs","cab"], groups = [1,2,2]))
#
# print(func(words=['a', 'b', 'r', 'fds', 'rtt', 'sd', 'a', 'dsad', 'r', 'u'], groups=[1, 1, 1, 4, 5, 6, 1, 8, 2, 2]))




s1 = 'abc'
s2 = 'abc'
print(s1 == s2)
test = ["bab","dab","cab", "tar", 'tab']
res = []

#
#
# #!!!!!!!#!!!!!!!
# def check_hemming(let1, let2):
#     if len([s for s in list(map(lambda x: set(x), zip(let1, let2))) if len(s) == 2]) == 1:
#         return True
#     return False
#
#
# final_res = []
# for let in range(len(test)):
#     temp = [test[let]]
#     for second_let in range(let + 1, len(test)):
#         if check_hemming(test[let], test[second_let]):
#             temp.append(test[second_let])
#     if len(temp) > len(final_res):
#         final_res += temp
# print(final_res)
#
# #!!!!!!!#!!!!!!!#!!!!!!!
#
#
# test_set = [{'d', 'b'}, {'a'}, {'b'}] # проверить наличие ТОЛЬКО одного множества длиной = 2

