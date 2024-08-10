def solution(brown, yellow):

    for width in range(3, brown //2):
        if (brown+yellow)%width == 0:
            for height in range(3, brown//2):
                if width*height == brown+yellow and width >= height and (width-2)*(height-2)==yellow:
                    return [width, height]