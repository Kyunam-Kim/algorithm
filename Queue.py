def put(item):
    queue.append(item)

def get():
    return queue.pop()

if __name__=='__main__':
    queue = []
    put(1)
    put(2)
    put(3)
    put(4)

    print("Queue's model")
    print(queue)
    
    while queue:
        print("POP > {}".format(get()))