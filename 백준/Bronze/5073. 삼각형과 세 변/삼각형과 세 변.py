while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    if a == b == c : 
        print("Equilateral")
    elif (a == b and b != c) or (a == c and a != b) or (b == c and a != b):
        l = [a, b, c]
        l.sort()
        if l[2] >= l[1]+l[0]:
            print("Invalid")
        else: print("Isosceles")
    elif a != b and b != c and c != a:
        l = [a, b, c]
        l.sort()
        if l[2] >= l[1]+l[0]:
            print("Invalid")
        else:
            print("Scalene")