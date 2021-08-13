# 패키지

# 패키지 : 도트(.)를 이용해 파이썬 모듈을 계층적으로 관리할 수 있게 함
# A.B -> A는 패키지명, B는 A 패키지의 모듈
# 패키지 -> 디렉터리, 파이썬 모듈로 구성

# Package_game은 루트 디렉토리, graphic과 sound는 서브 디렉토리



# 1. 패키지를 이용해 echo.py 파일의 Echo_Test 함수 실행하는 방법 세 가지

# a. 모듈을 import하여 실행
import Package_game.sound.echo # 루트 디렉토리 Package_game, 서브 디렉토리 sound, 그 안의 echo.py를 가져옴
Package_game.sound.echo.Echo_Test()

# b. 모듈이 있는 디렉토리까지 from ~ import ~ 하여 실행
from Package_game.sound import echo
echo.Echo_Test()

# c. 모듈의 함수를 직접 import하여 실행
from Package_game.sound.echo import Echo_Test
Echo_Test()



# 2. __init__.py의 용도
# __init__.py 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할
# 디렉토리에 __init__.py가 없으면 패키지로 인식되지 않는다. (중요)



# 3. __all__의 용도
# 특정 디렉토리의 모듈을 *을 이용하여 import할 때는
# 해당 디렉토리의 __init__.py 파일에 __all__이라는 변수를 설정하고
# import할 수 있는 모듈을 리스트 형태로 정의해줘야 한다.
from Package_game.sound import *
echo.Echo_Test()



# 4. relative 패키지
# .. -> 부모 디렉토리
# . -> 현재 디렉토리

# from ..sound.echo import ~ 라고 하면
# 부모 디렉토리의 sound 폴더에 echo 모듈을 가져올 수 있다.
# relative한 접근자는 모듈 안에서만 사용해야 한다.