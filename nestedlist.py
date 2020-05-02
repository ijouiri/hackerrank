if __name__=="__main__":
    all = list()
    for _ in range(int(input())):
        name=input()
        score=float(input())
        all.append([name,score])

    second_high_score = sorted(set([i for a , i in all]))[1]

    print ("\n".join(sorted([a for a , k in all if k==second_high_score])))