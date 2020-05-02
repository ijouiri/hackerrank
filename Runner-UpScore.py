if __name__=="__main__":
    n = int(input())
    arr =list(map(int, input().split()))
    maxnumber=max(arr)
    while True :
        if maxnumber==max(arr):
            arr.remove(max(arr))
        else :
            break
    print (max(arr))
