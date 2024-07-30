def solution(nums):
    answer = 0
    choose = int(len(nums)/2)
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
    if len(arr) >= choose:
        return choose
    else:
        return len(arr)