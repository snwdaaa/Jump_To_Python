# 딕셔너리
# 대응 관계를 나타내는 자료형 => 연관 배열(Associative Array), 해시(Hash)
# 파이썬에서는 딕셔너리(Dictionary)라고 부름
# 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형
# 리스트나 튜플처럼 순차적으로 해당 요소값을 구하지 않고 Key를 통해 Value를 얻음 (가장 큰 특징)

# 1. 딕셔너리 선언
# key와 value의 여러 쌍이 {}로 둘러싸임
# key는 변하지 않는 값이고, value는 변하는 값, 변하지 않는 값 둘 다 사용 가능
# {key1:value1, key2:value2, key3:value3, ...} 형태
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a = {1:'hi'} # key로 정수값, value로 문자열
b = {'a':[1,2,3]} # key로 문자열, value로 리스트



# 2. 딕셔너리 추가 & 삭제
# 딕셔너리는 순서를 따지지 않는다는 사실을 기억

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b' # 딕셔너리 a에 2:'b' 추가
a['name'] = 'pey' # 딕셔너리 a에 'name':'pey' 추가
print(a)

# 딕셔너리 요소 삭제하기
# del 딕셔너리[key]
del a[1] # 딕셔너리 a에서 key가 1인 {key:value} 쌍 삭제
print(a) # {2:'b', 'name':'pey'}



# 3. Key를 사용해 Value 얻기 -> 딕셔너리변수[key]
# 딕셔너리에서는 [] 안의 값이 index가 아니라 key라는 것을 꼭 기억하자
grade = {'pey':10, 'julliet':99}
print(grade['pey']) # 10
print(grade['julliet']) # 99



# 4. 딕셔너리 주의사항
# key는 고유한 값이므로 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다(어떤 것이 무시될 지는 예측 X)
# => 중복되는 Key를 쓰지 말자

# key에는 리스트가 올 수 없다. 하지만 튜플은 올 수 있다. (key에는 고정된 값만 올 수있기 때문)



# 5. 딕셔너리 관련 함수

# Key 리스트 만들기 -> 딕셔너리.keys() : 딕셔너리의 key만 모아서 dict_keys라는 객체를 리턴
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.keys())
dict_keys_list = list(a.keys()) # dict_keys 객체를 list로 변환
print(dict_keys_list)

# Value 리스트 만들기 -> 딕셔너리.values() : 딕셔너리의 value만 모아서 dict_values라는 객체를 리턴
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.values())
dict_values_list = list(a.values()) # dict_values 객체를 list로 변환
print(dict_values_list)

# Key, value 쌍 얻기 -> 딕셔너리.items() : key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴
print(dic.items())
dict_items_tuple = tuple(dic.items()) # dict_items 객체를 tuple로 변환
print(dict_items_tuple)

# key:value 쌍 모두 지우기 -> 딕셔너리.clear() : 딕셔너리 안의 모든 요소를 삭제. 빈 딕셔너리를 {}로 표현
dic.clear()
print(dic)

# Key로 Value 얻기 -> 딕셔너리.get(key) : key에 대응되는 value를 리턴. 딕셔너리[key]와 동일한 역할
# 인수로 없는 key를 주면, None(거짓) 리턴 
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))
# 찾으려는 key 값이 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져올 수 있음
# 딕셔너리.get(key, 디폴트값)
print(a.get('foo', 'bar'))

# key가 딕셔너리 안에 있는지 조사하기 -> in 키워드
print('name' in a) # True
print('email' in a) # False