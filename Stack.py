def push(item):
    stack.append(item)

def pop():
    return stack.pop()

if __name__=='__main__':
    stack = []
    push(1)
    push(2)
    push(3)
    push(4)
    print("Stack's model")
    print(stack)

    while stack:
        print("POP > {}".format(pop()))