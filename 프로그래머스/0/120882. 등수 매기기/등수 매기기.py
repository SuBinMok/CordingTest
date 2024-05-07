def solution(score):
    answer = []
    avg_score = [0] * len(score)
    for i in range(len(score)):
        avg_score[i] = (score[i][0] + score[i][1])/2
    s1 = sorted(avg_score, reverse = True)
    for i in avg_score:
        answer.append(s1.index(i)+1)
    return answer