def solution(genres, plays):
    answer = []
    p = {}
    arr = []
    for i in range(len(genres)):
        arr.append([i, genres[i], plays[i]])
    arr = sorted(arr, reverse = True, key = lambda x: x[2])
    for i in range(len(genres)):
        if arr[i][1] in p:
            p[arr[i][1]] += arr[i][2]
        else:
            p[arr[i][1]] = arr[i][2]
    for i, v in sorted(p.items(), reverse = True, key = lambda x: x[1]):
        k = 0
        for j in range(len(genres)):
            if arr[j][1] == i and k < 2 and v >= 0:
                answer.append(arr[j][0])
                v -= arr[j][2]
                k += 1
    return answer