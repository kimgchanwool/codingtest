def solution(participant, completion):
    answer = {}
    for i in participant:
        if i in answer.keys():
            answer[i] += 1
        else:
            answer[i] = 1
    for j in completion:
        if answer[j] != 1:
            answer[j] -= 1
        else:
            del answer[j]
    print(answer)
    return list(answer)[0]
if __name__ == '__main__':
    print(solution(['a', 'b', 'c' ,'d' ,'e'], ['a', 'c', 'd', 'e']))
