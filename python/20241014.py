# 회문 문자열검사
# N개의 문자열 데이터를 입력받아
# 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문문자열)
# 이면 Yes를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램
# 단 회문을 검사할때 대소문자를 구분하지 않습니다.

# 입력설명
# 첫줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄 부터
# N개의 단어가 입력된다 각 단어의 길이는 100을 넘지 않는다

# 출력설명
# 각줄에 해당 문자열의 결과를 Yes 또는 No로 출력한다.

# 입력예제1
"""
5
level
moon
abcba
soon
gooG

yes
no
yes
no
yes
"""
import sys

n = int(input())
for i in range(n):
    s = input()
    # 모두 대문자로변경
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %i+1)
            break
    else:
        print("#%d Yes" %(i+1))

# for ~ else 
# for문이 정상적으로 끝났으면 else 문을 실행하게 된다.


'''
# 2

s[::-1] -> 문자열을 거꾸로 하는코드
if s == s[::-1]:
    print("#%d Yes", %(i+1))
else:
    print("#%d NO", %(i+1))
'''
