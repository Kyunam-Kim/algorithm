def f(n):
    if n > 1:
        f(n-1)
    print(n)

if __name__=='__main__':
    f(20)