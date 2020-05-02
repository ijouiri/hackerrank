if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        sizeA, A, sizeB, B = input(), set(input().split()), input(), set(input().split())

        print (A.issubset(B))
