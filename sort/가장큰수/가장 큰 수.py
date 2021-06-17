def solution(numbers):
    answer = ''; num = [];
    """
    for i in numbers:
        if i < 10:
            num.append(i)
        else:
            while i >= 10: #10보다 큰 경우 앞자리 수만 봐야함.
                num.append(i % 10)
                i /= 10
            num.append(int(i))
    num.sort(reverse=True)
    num = "".join(str(i) for i in num) #"".join은 리스트를 문자열로 변환.
    """
    #다르게 생각하자 문자열로 변환하고 첫번째 인덱스로 비교해보자.
    for i in numbers:
        num.append(str(i))
    #num = sorted(num,reverse=True)
    num.sort(key=lambda x: x*3, reverse=True)
    num =  str(int("".join(i for i in num)))

    #이코드 문제점 30과 3일때 비교안됌
    return num;

if __name__ == "__main__":
    numbers =[]
    solution(numbers)