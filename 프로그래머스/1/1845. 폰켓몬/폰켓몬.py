def solution(nums):
    nl = list(set(nums))
    if (len(nums)/2) < len(nl):
        return int(len(nums)/2)
    return len(nl)