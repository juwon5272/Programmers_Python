# 배열의 평균값
# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum/len(numbers)
