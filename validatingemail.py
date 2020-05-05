# check if has a format like email@domain.extension

# the username can only contain letters , digits ,dashes , and underscores

# the domain name can only have letters and digits

#max length of extension is 3

def fun1(n):
    try:
        username,domain = n.split('@')
        domain , extension = domain.split('.')
    except :
        return False
    if (username.replace('_','').replace('-','').isalnum()) is False:
        return False
    if (domain.isalnum()) is False:
        return False
    if len(extension) > 3:
            return False
    else :
        return True
def emailfilter (email):
    return list(filter(fun1,email))
if __name__=="__main__":
    n = int(input())
    emaillist=list()
    for _ in range(n):
        emaillist.append(input())

    ee=emailfilter(emaillist)
    ee.sort()
    print (ee)
