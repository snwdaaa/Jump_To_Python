# 모듈

# 모듈 : 함수, 변수, 클래스를 모아놓은 파일
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만들어진 파이썬 파일

# 모듈 가져오기 -> import 명령어
# import 모듈이름(파일이름)
# import는 모듈을 호출하는 파일과 같은 디렉토리에 있거나
# 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다. (중요)

# 모듈에 있는 함수를 사용하려면 모듈이름.함수 이런식으로 사용할 수 있다.

import module_declaration # module_declaration.py 파일을 import 함

print(module_declaration.Sum(1,2))
print(module_declaration.SafeSum(1,2))
print(module_declaration.SafeSum(1,'a'))

# 도트 연산자 없이 함수 쓰는 법
# from 모듈이름 import 모듈함수
from module_declaration import SafeSum # module_declaration.py에서 SafeSum 함수만 가져옴
from module_declaration import SafeSum, Sum # 함수 여러 개 가져오기
from module_declaration import * # *: 모든 함수를 가져온다.

# 도트 연산자 없이 import한 함수 사용 가능
print(SafeSum(1,2))
print(SafeSum(1,'a'))

# 모듈에 포함된 변수, 클래스 사용하기
print(module_declaration.PI)

a = module_declaration.Math()
print(a.Solve(10))