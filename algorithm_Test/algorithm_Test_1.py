# 반복문을 사용하여 0부터 n까지의 합 출력

def print_to_n(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    # i = 0
    # while i <= n:
    #     sum += i
    #     i = i + 1
    print(sum)

if __name__=='__main__':
    print_to_n(10)