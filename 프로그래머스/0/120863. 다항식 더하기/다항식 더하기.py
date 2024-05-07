def solution(polynomial):
    answer = ''
    s = polynomial.split()
    s = [i for i in s if i != '+']
    x = 0
    n = 0
    for i in s:
        if 'x' == i:
            x+=1
        elif 'x' in i:
            x+=int(i[:-1])
        else:
            n += int(i)
    if x != 0 and n != 0:
        if x == 1:
            answer = 'x'+' + ' + str(n)
        else:
            answer = str(x)+'x'+' + '+str(n)
    elif x != 0 and n == 0:
        if x == 1:
            answer = 'x'
        else:
            answer = str(x)+'x'
    elif x == 0 and n != 0:
        answer = str(n)
    # else:
    #     answer = str(0)
    return answer