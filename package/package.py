# 재사용 가능한 모듈의 집합, 모듈이 뭉쳐있는 폴더
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성된다.
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

import sub.sub1.module1
import sub.sub2.module2

# 같은 경로에 있으면 경로에서 append 해서 사용하지 않고 import 로 바로 접근해서 ( . )으로 사용할 수 있다.
# sub.sub1.module1.mod1_test

# sub 패키지 하위에 sub1 패키지 하위에 module1 모듈을 import 해온다.
# 모듈의 이름이 길어지면 from 절을 사용할 수 있다.
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias

# from 절을 사용해서 import 하면
module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

# 이런 방식으로 사용할 수 있다.

# * 는 사용하지도 않을건데 다 가져올 필요는 없다. (불필요한 작업, 사용할거만 정확하게 가져오는게 더 효율적)
from sub.sub1 import *
from sub.sub2 import module2

module1.mod1_test1()
module2.mod2_test1()

#패키지 안에는 __init__.py 가 있다. 이것은 python 3.3 부터는 없어도 패키지로 인식한다. 단 하위호환을 위해 작성을 추천한다. !
# 3.3 이전에는 __init__.py 가 없으면 패키지 인식이 안됐다.
# 내용은 __all__ = ['module1', 'module2']  import 허가되는 모듈이름의 목록을 의미한다.