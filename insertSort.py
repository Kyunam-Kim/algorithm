# import random
# import time

# compare_counter = 0
# swap_counter = 0

# def insertion_sort(my_list):
#     global compare_counter, swap_counter
#     my_list.insert(0, -1)
#     for idx in range(2, len(my_list)):
#         temp = my_list[idx]
#         while my_list[idx] > temp:
#             my_list[idx] = my_list[idx - 1] 
#             idx = idx - 1
#     del my_list[0]

# if __name__=='__main__':
#     list = []
#     for i in range(10):
#         list.append(random.randint(1, 10))
#     print("<Before Sort>")
#     print(list)
#     insertion_sort(list)
#     print("<After sort")
#     print(list)
#  수정필요