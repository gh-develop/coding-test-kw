a, b = input().split()

result = max(int(a[::-1]),int(b[::-1]))

print(result)


'''문자열을 역으로 출력하는 방법 3가지 
1. a[::-1]
2. reverse ---> reverse는 값을 반환하지 않고 , 단순히 해당 list를 역순으로 섞는다. reverse는 list타입에만 적용된다.
3. reversed ----> str에도 적용가능 
2, 3번은 join으로 다시 붙여줘야댐
https://velog.io/@luke/2908.-상수-백준-알고리즘-파이썬 참고하자 ㅇㅇ
'''