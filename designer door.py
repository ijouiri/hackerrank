if __name__=="__main__":
    a, b=map(int,input().split())

    for i in range(a//2):
        print ((".|."*((i*2)+1)).center(b,"-"))
    print ("WELCOME".center(b,"-"))
    for i in range (a//2,0,-1):
        print((".|." * ((i*2)-1)).center(b, "-"))
