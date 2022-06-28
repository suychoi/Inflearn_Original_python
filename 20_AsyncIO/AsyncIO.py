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


















