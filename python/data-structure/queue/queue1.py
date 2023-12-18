import queue

def hot_potato(name_list,num):
    q = queue.Queue()
    for name in name_list:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        
        q.dequeue()

    return q.dequeue()


if __name__ == '__main__':
    list_nya = ["Bill","David","Susan","Jane","Kent","Brad"]
    print(hot_potato(list_nya,7))