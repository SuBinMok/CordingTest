def solution(numbers):
    answer = ''
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for i in range(len(numbers)):
        if  numbers[i:i+4] == "zero":
            answer+="0"
        elif numbers[i:i+3] == "one":
            answer+="1"
        elif numbers[i:i+3] == "two":
            answer+="2"
        elif numbers[i:i+5] == "three":
            answer+="3"
        elif numbers[i:i+4] == "four":
            answer+="4"
        elif numbers[i:i+4] == "five":
            answer+="5"
        elif numbers[i:i+3] == "six":
            answer+="6"
        elif numbers[i:i+5] == "seven":
            answer+="7"
        elif numbers[i:i+5] == "eight":
            answer+="8"
        elif numbers[i:i+4] == "nine":
            answer+="9"
        else:
            continue
    return int(answer)