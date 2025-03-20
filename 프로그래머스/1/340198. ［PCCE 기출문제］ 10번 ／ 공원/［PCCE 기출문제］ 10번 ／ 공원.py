def solution(mats, park):
    answer = 0
    mats = sorted(mats, reverse = True)
    m, n = len(park), len(park[0])
    for mat in mats:
        start_idx = set((i, j) for i in range(m-mat+1) for j in range(n-mat+1))
        for a, b in start_idx:
            place = set()
            for i in range(a, a+mat):
                for j in range(b, b+mat):
                    place.add(park[i][j])
            if place == {'-1'}:
                return mat
    return -1