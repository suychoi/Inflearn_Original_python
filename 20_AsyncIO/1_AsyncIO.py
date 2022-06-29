'''
AsyncIO 실습
 - 가상환경 생성
 - 타겟 사이트 살펴보기
 - 프로그램 설명
 - async, await 설명
 - 프로그램 테스트

AsyncIO : 비동기  I/O Coroutine 작업을 쉽게 하는 패키지,
Generator 는 반복적인 객체 return을 사용
Non-Blocking 비동기 처리

Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때 까지 제어권을 갖고있어서, 타 함수는 대기함
Non-Blocking I/O : 호출된 함수(서브루틴)가 return 후 호출한 함수( 메인 루틴) 에 제어권 전달 -> 타 함수는 일 지속가능

내가 사용할 함수도 blocking 함수( 제네레이터 같은? ) 인지 확인하고 그에 맞게 스레드를 사용할지 말지 확인 ..

Thread 단점 : 디버깅, 자원 접근 시 레이스컨디션(경쟁상태), 데드락(Dead Lock) -> 고려 필요
코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요 없음. 제어권으로 실행 -> 스레드의 단점 고려 필요 없음
코루틴 단점 : 사용함수가 비동기로 구현이 되어 있어야 함!
'''

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
start = timeit.default_timer()

#서비스 방향이 비슷한 사이트로 실습 권장( 예 : 게시판성 커뮤니티)
urls = ['http://daum.net',
        'https://naver.com',
        'http://mlbpark.donga.com',
        'https://tistory.com',
        'https://wemakeprice.com']

# urlopen 함수는 Block I/O 이다. 그래서 Thread를 사용해서 urlopen 을 따로 사용해준다면,
# asyncio 에서 다른 사이트에서 응답이 올 때 까지 제어권을 넘기도록(yield, generator) 코딩

async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)

    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)     # urlopen 함수 non-block으로 만들어줌.
    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)  # 시작순서와 종료순서가 다름.
    # 결과 반환
    return res.read()[:5]


async def main():   # 비동기 함수
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취함
    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)


if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop() # 제어권을 서로 주고받고 하겠다!

    # 작업 완료까지 대기
    loop.run_until_complete(main())

    # 수행 시간 계산
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total running time : ', duration)
















