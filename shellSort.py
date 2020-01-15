import random
import time

def shell_sort(random_list):
    h = 1
    while h < len(random_list):
        h = h*3 + 1
    h = h//3

    # while h > 0:
    #     for i in range(h):
    #         start_index = i + h

    #         while start_index < len(random_list):
    # 수정 필요