# https://school.programmers.co.kr/learn/courses/30/lessons/12931

import math


def solution(n):
    answer = 0

    while n/10 != 0:
        answer = answer+math.floor(n % 10)
        n = n/10

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
