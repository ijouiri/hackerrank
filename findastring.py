def counter (string , substring):
    sum = 0
    for i in range(len(string)) :
        try:
            if (string[i:i+len(substring)])==substring :
                sum +=1
        except :
            pass
    return sum
if __name__ == '__main__':
    string , substring = (input().strip(),input().strip())

    print (counter(string, substring))

