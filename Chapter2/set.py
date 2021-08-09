# 집합에 관련된 것들을 쉽게 처리하는 자료형

# 1. 집합 자료형 선언 -> set 키워드
# set의 인수로 리스트 or 튜플를 입력한다.
s1 = set([1, 2, 3])
print(s1)
# 문자열도 입력할 수 있다.
s2 = set("Hello")
print(s2) # 순서는 매번 바뀜

# set의 특징
# 1. 중복 허용 X
# 2. 순서 X (unordered) -> 인덱싱으로 값을 얻을 수 없음
# => 집합 자료형의 값을 인덱싱으로 접근하려면, 집합을 리스트나 튜플로 변환해야 한다.
s1 = set([1,2,3])
list1 = list(s1) # 리스트로 변환
print(list1)
print(list1[0])
tuple1 = tuple(s1) # 튜플로 변환
print(tuple1)
print(tuple1[1])



# 2. 집합 자료형 활용

# 합집합, 교집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

set_union = s1 | s2 # 합집합 -> |(or) 기호 이용
set_union = s1.union(s2) # 또는 union 함수 사용
print(set_union) # {1,2,3,4,5,6,7,8,9}

set_intersection = s1 & s2 # 교집합 -> &(and) 기호 이용
set_intersection = s1.intersection(s2) # 또는 intersection 함수 사용
print(set_intersection) # {4,5,6}

set_diff = s1 - s2 # 차집합 -> - 기호 이용
set_diff = s1.difference(s2) # 또는 difference 함수 사용
print(set_diff) # {1,2,3} -> s1에서 s2를 뺀거



# 3. 집합 관련 함수

# 값 1개 추가하기 -> 집합.add(x) : 이미 만들어진 집합에 x를 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가하기 -> 집합.update(리스트 or 튜플) : 이미 만들어진 집합에 리스트나 튜플의 원소를 추가
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기 -> 집합.remove(x) : 집합 안에 있는 값 x 제거
s1 = set([1,2,3])
s1.remove(2)
print(s1)