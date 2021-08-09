# 새로 배운 것 -> or-not-and, in-not in, pass, elif

# if문

# 1. if문의 기본 구조
# 파이썬은 들여쓰기가 중요하다
# if 조건문:
#   수행할 문장1 # 들여쓰기 한 문장들은 if문의 블럭 안에 있는 것
#   수행할 문장2
#   ...
# else:
#   수행할 문장A
#   수행할 문장B
#   ...
money = 1
if money:
    print("택시를 타고 간다.")
else:
    print("걸어간다.")

# 비교연산자 이용
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 논리 연산자 and, or, not
# C언어에서의 |, &, ! => 파이썬에서 or, and, not
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# in과 not in (중요)
# x in 리스트, x not in 리스트
# x in 튜플, x not in 튜플
# x in 문자열, x not in 문자열
# x가 리스트,튜플,문자열 안에 있다면 True, 없으면 False 반환
print(1 in [1,2,3])
print(1 not in [1,2,3])

# 응용
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: # pocket 리스트 안에 'money' 요소가 있는지 확인
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# pass 키워드 -> 조건문에서 아무런 일도 하지 않는다.
if 'money' in pocket: # pocket 리스트 안에 'money' 요소가 있는지 확인
    pass # 아무 것도 하지 않는다.
else:
    print("걸어 가라")

# else if문 -> elif
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket: # pocket 리스트 안에 'money' 요소가 있는지 확인
    print("택시를 타고 가라")
elif card: # else if card
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if문 한 줄에 쓰기
if 'money' in pocket: pass
elif card: print("택시를 타고 가라")
else: print("걸어 가라")
