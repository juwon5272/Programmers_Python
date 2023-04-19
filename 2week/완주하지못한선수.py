# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 완주하지 못한 선수
# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

def solution(participant, completion):
    Dict = {}
    sum = 0

    for part in participant:
        Dict[hash(part)] = part
        sum += hash(part)

    for com in completion:
        sum -= hash(com)

    return Dict[sum]