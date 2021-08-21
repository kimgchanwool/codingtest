def solution(phone_book):
    answer = True
    phones = dict()
    for phone_num in phone_book:
        phones[phone_num] = 1
    for phone_num in phone_book:
        temp = ''
        for num in phone_num:
            temp += num
            if temp in phones and temp != phone_num: #자신에게 파생된 것이 자신과 같으면 안된다.
                return False
    return answer



def solution2(phone_book):
    answer = True
    for i_index, i in enumerate(phone_book):
        for j_index, j in enumerate(phone_book):
            if (i in j or j in i) and i_index != j_index and len(i) < len(j) and i[:len(i)] == j[:len(i)]:
                answer = False
            elif (i in j or j in i) and i_index != j_index and len(i) > len(j) and j[:len(j)] == i[:len(j)]:
                answer = False
    return answer

if __name__ == '__main__':
    a = list(input().split())
    print(solution(a))

