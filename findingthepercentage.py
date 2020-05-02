if __name__=='__main__':
    n = int(input())
    storage = {}
    for _ in range(n):
        name , *line = input().split()
        score = list(map(float,line))
        storage[name]=sum(score)/3

    get_name=input()

    if get_name in storage:
        print ('%.2f' % storage[get_name])