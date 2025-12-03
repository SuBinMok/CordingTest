import sys

"""
손님이 받는 동전 갯수를 최소화 하고자 함 : 가장 큰 동전부터 처리하기.
잔돈은 항상 5달러 미만
쿼터 : 0.25, 다임 : 0.10, 니켈 : 0.05, 페니 : 0.01
"""
num = int(sys.stdin.readline())
quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(num):
    c = int(sys.stdin.readline())
    quarter_num = c // quarter
    c -= quarter*quarter_num
    dime_num = c//dime
    c -= dime_num*dime
    nickel_num = c //nickel
    c -= nickel_num*nickel
    penny_num = c //penny

    print(quarter_num, dime_num, nickel_num, penny_num)

