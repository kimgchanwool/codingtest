def solution(participant, completion):
    answer = ''
    a, b = dict(), dict()
    completion.append('None')
    for i, j in zip(participant, completion):
        if i in a.keys():
            a[f'{i}'] += 1
        else:
            a[f'{i}'] = 1
        if j == 'None':
            break
        elif j in b.keys():
            b[f'{j}'] += 1
        else:
            b[f'{j}'] = 1
    for i in a:
        if i not in b or a[i] != b[i]:
            return i
    return answer

def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]

if __name__ == '__main__':
    print(solution(['a', 'b', 'c' ,'d' ,'e'], ['a', 'c', 'd', 'e']))
