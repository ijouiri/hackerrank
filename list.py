# def _insert(pos , number):
#     return l.insert(pos,number)
# def _print():
#     print(l)
# def _remove(var):
#     return l.remove(var)
# def _append (num ):
#     return l.append(num)
# def _sort():
#     return l.sort()
# def _pop():
#     return l.pop()
# def _reverse ():
#     return l.reverse()
# l = []
# if __name__=="__main__":
#     n =int(input())
#     for _ in range(n):
#         command , *number = input().split()
#         change = list(map(int , number))
#         if command == 'print':
#             _print()
#         elif command == 'insert':
#             _insert(change[0],change[1])
#         elif command == "remove":
#             _remove(change[0])
#         elif command == "reverse":
#             _reverse()
#         elif command == "pop":
#             _pop()
#         elif command == "sort":
#             _sort()
#         elif command == "append":
#             _append(change[0])


#lets try another way to solve this problem

l = []
if __name__=='__main__':
    n = int(input())
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        all = s[1:]
        var=','.join(all)
        if cmd == "print":
            print (l)
        else:
            eval('l.'+cmd+'('+var+')')


#test condition :
"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

"""