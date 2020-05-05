curb = lambda x : x**3
def fibonacci(n):

    vslist=[0,1]
    if n ==0 :
        return 0
    elif n == 1 :
        yield 0
    else :

        for i in range(2,n):
            vslist.append(vslist[i-2]+vslist[i-1])

        for i,k in enumerate (vslist):
            yield k
if __name__=="__main__":
    n = int(input())
    print (list(map(curb,fibonacci(n))))
