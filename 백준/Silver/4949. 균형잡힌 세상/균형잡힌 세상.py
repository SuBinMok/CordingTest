import sys

while True:
    a = sys.stdin.readline().rstrip()
    s_list = []
    if len(a) == 1 and a == ".":
        break
    for i in a:
        if i == '(' or i == '[':
            s_list.append(i)
        elif i == ')':
            if len(s_list) != 0 and s_list[-1] == '(':
                s_list.pop()
            else:
                s_list.append(i)
                break
        elif i == ']':
            if len(s_list) != 0 and s_list[-1] == '[':
                s_list.pop()
            else:
                s_list.append(i)
                break

    if len(s_list) == 0:
        print("yes")
    else:
        print("no")