#the first method to solve the problem with math :

# if __name__=="__main__":
#     n = int(input())
#     roomnumbers=list(map(int,input().split()))
#
#     rmnr = set(roomnumbers) #room numbers not repeted
#     print(((sum(rmnr)*n)-(sum(roomnumbers)))//(n-1))


# the second method its just a logic algorithm :

if __name__ == "__main__":
    n,rooms,singleroom,multiroom=input(),input().split(),set(),set()

#i don't know how to do with this method yat so i will try it after i post this on hackerrank



    # [singleroom.add(k) for k in rooms if not k in singleroom else '']

    for k in rooms:
        if not k in singleroom:
            singleroom.add(k)
        else :
            multiroom.add(k)


    fin=singleroom.difference(multiroom)
    print (''.join(fin))
