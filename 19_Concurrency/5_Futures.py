'''
Futures(동시성)
 - Futures wait 예제
 - Futures as_completed
 - 동시 실행 결과 출력
 - 동시성 처리 응용 예제 설명

    비동기 작업 실행
    지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업에서 동시성 활용 권장
    비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상됨.

    futures : 비동기 실행을 위한 API를 고수준으로 작성하던 내용을 사용하기 쉽도록 개선
    concurrent.Futures 3.2버전부터
    1. 멀티스레딩/멀티프로세싱 API 통일 -> 사용하기 쉬워짐
    2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성(Promise 개념)

    2가지 패턴 실습
    concurrent.futures map
    concurrent.futures wait, as_completed

    # wait 은 시간을 제어할 수 있고, 기다릴 수 있다.
    # as_completed 는 먼저 끝나는 대로 반환합니다.

    GIL : 파이썬에만 있는 특징, Global interpreter lock, 두개 이상의 스레드가 동시에 실행될 때 하나의 자원을
        엑세스 하는 경우 -> 문제점을 방지하기 위해 GIL 실행, 리소스 전체에 락이 걸린다.
        -> Contect Switch(문맥 교환)
    GIL 우회 : 멀티프로세싱 사용, CPython
'''

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [10000, 100000, 1000000, 10000000]

#동시성 합계 계산 메인 함수
# 누적 합계 함수(Generator)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

# wait
# as_completed
def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_tm = time.time()
    #Futures
    futures_list = []

    # 결과 건수( ProcessPoolExecutor or ThreadPoolExecutor ) 바꿔치기
    with ProcessPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환( 미래에 할 일 반환)
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케줄링 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()

        '''    
        # Wait 결과 출력    
        result = wait(futures_list, timeout=5)
        # 성공 확인
        print('Completed Tasks : ' + str(result.done))  # state=finished 확인
        # 실패 확인
        print('Failed Tasks : ' + str(result.not_done))  # 5초 이상 걸리는
        # 결과 값 출력
        print([future.result() for future in result.done])
        '''

        # as_completed 결과 출력 ( 먼저 끝나는걸 먼저 출력 )
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포멧
    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(end_tm))

# 실행
if __name__ == '__main__':      # 시작점을 명시적으로 작성해야 멀티프로세싱이 된다.
    main()











