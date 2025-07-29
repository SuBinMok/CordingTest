import sys

girl, question = map(int, sys.stdin.readline().split())
group = {}
member = {}
for _ in range(girl):
    g = str(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline())
    group[g] = []
    for _ in range(N):
        person = str(sys.stdin.readline().rstrip())
        group[g].append(person)
        member[person] = g
    group[g] = sorted(group[g])
for _ in range(question):
    q = str(sys.stdin.readline().rstrip())

    if int(sys.stdin.readline()):
        print(member[q])
    else:
        print('\n'.join(group[q]))