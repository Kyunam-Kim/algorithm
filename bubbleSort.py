import random
import time

compare_counter = 0
swap_counter = 0

def bubble_sort(random_list):
    for start_index in range(len(random_list) - 1):
        for index in range(1, len(random_list) - start_index):
            if random_list[index - 1] > random_list[index]:
                temp = random_list[index - 1]
                random_list[index - 1] = random_list[index]
                random_list[index] = temp

if __name__=='__main__':
    list = []
    input_n = input("Sorted data number")
    for i in range(int(input_n)):
        list.append(random.randint(1,int(input_n)))
    print("Before sort")
    print(list)

    start_time = time.time()
    bubble_sort(list)
    running_time = time.time() - start_time

    print("After sort")
    print(list)

    print("data size: {}".format(int(input_n)))
    print("compare counter: {}".format(compare_counter)
    print("swap counter: {}".format(swap_counter)
    print("running time: {}".format(running_time)
