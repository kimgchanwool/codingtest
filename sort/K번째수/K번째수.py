def solution(array, commands):
    answer = []; nums=[]; num = []
    for x,y,z in commands:
        num = array[x-1:y]
        num.sort()
        answer.append(num[z-1])
    return answer

if __name__ == "__main__":
    array = []
    commands = []
    print(solution(array, commands))