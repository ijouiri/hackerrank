if __name__=="__main__":
    a = set(input().split())
    listemety = []
    for _ in range(int(input())):
        listemety.append(set(input().split()).issubset(a))

    print(all(listemety))