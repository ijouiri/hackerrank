if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
add=[[i,k,i] for i in range (x+1) for k in range (y+1) for m in range (z+1) if i+m+k!=n]
print (add)



# )( m for m in range (y+1) )(k for k in range (z+1)) if i+m+k !=n else ''
