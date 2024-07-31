def solution(genres, plays):
    answer = []
    playlist = {}
    arr = []
    num = len(genres)
    for i in range(num):
        arr.append([i, genres[i], plays[i]])
    arr = sorted(arr, reverse = True, key = lambda x: x[2])
    for i in range(num):
        if arr[i][1] in playlist:
            playlist[arr[i][1]] += arr[i][2]
        else:
            playlist[arr[i][1]] = arr[i][2]
    for item, values in sorted(playlist.items(), reverse = True, key = lambda x: x[1]):
        k=0
        for i in range(num):
            if arr[i][1] == item and k<2 and values >= 0:
                answer.append(arr[i][0])
                values -= arr[i][0]
                k += 1
    return answer