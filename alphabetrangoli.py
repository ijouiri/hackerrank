l=list()
newlist=list()

if __name__=="__main__":
    n=int(input())
    k=97
    for i in range (n):
        l.append(chr(k))
        k+=1
    for i in range(n):
        s="-".join(l[i:n])
        newlist.append((s[::-1]+s[1:]).center(4*n-3,'-'))

    print ("\n".join(newlist[::-1]+newlist[1:]))

    # -- or --
   # for i in reversed(newlist):
   #     print (i)
   # for i in newlist[1:]:
   #     print (i)

