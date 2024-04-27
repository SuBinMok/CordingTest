a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
if a1 == a2 :
    print(a3, end=" ")
elif a1 == a3:
    print(a2, end=" ")
elif a2 == a3:
    print(a1, end=" ")
if b1 == b2 :
    print(b3, end=" ")
elif b1 == b3:
    print(b2, end=" ")
elif b2 == b3:
    print(b1, end=" ")    