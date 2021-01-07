#regular equation 정규식

"""
주민등록번호
970821-1111111

이메일 주소
ech97@naver.com

이런식의 간단한 형식들이있음
"""

import re

p = re.compile("ca.e")
# . : 은 하나의 문자를 의미 > (ca.e) care, cafe, case
# ^ : 문자열의 시작 > (^de) desk, destination
# $ : 문자열의 끝 > (se$) case, base

def print_re(m):
    #print(m.group()) # 매치되지않으면 에러 발생
    if m:
        print("m.group()", m.group()) # 일치하는 문자열 반환
        print("m.string: ", m.string) # 입력받은 문자열 그대로 반환 > 얘는 함수아니라서 ()없다잉
        print("m.start(): ", m.start()) # 일치하는 문자열의 시작 ind
        print("m.end(): ", m.end()) # 일치하는 문자열의 끝 ind
        print("m.span(): ", m.span()) # 일치하는 문자열의 시작 / 끝 ind

    else:
        print("매칭되지 않음")

m = p.match("careless") # 주어진 문자열의 처음부분이 일치하는지 확인하는거라 뒤에 상관 x
print_re(m)

m = p.search("good care") # 주어진것중에 일치하는게 있는지 다 확인
print_re(m)

lst = p.findall("carelesscafe") # 일치하는 모든 것을 리스트 형태로 반환
print(lst)


"""
1. p = re.compile("찾고자하는 형태")
    # . : 은 하나의 문자를 의미 > (ca.e) care, cafe, case
    # ^ : 문자열의 시작 > (^de) desk, destination
    # $ : 문자열의 끝 > (se$) case, base

2. m = p.match("비교할 문자열") : 문자열의 처음부분이 같은건지 확인
   m = p.search("비교할 문자열") : 같은게 있는지 쭉 훑어서 최초발견 하나 찾기
   m = p.findall("비교할 문자열") : 해당하는 형태를 모조리 수집하여 리스트 형태로 반환

3. m.group() : 일치하는 문자열 출력
   m.string : 일치한다면 입력한거 다 출력
   m.span() : 일치하는 시작 끝 ind 반환

"""