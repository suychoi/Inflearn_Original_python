# Hangman mini game
import time
import csv
import random
import winsound # 소리 외장 패키지
# Game Start
name = input("Input your name : ")

print('Wellcome \"' + name + "\".", 'No escape untill \"GMAE OVER\"')

time.sleep(1)

print("Start Loading...")

time.sleep(0.5)

words = []
with open("../00_resource/word_list.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)
q = random.choice(words)    #[[][]]

word = q[0].strip() # 정답 설정 및 공백 제거
guesses = ''    # 추측 문자
turns = 10      # 기회

# 핵심, While
while turns > 0:
    failed = 0          #남은 비밀 문자
    # 정답단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되는 경우
        if char in guesses:
            # 추측단어 출력
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    # 단어 추측이 성공하는 경우
    if failed == 0:
        print()
        print()
        print('The Great Escape!')
        break

    #추측 단어 문자 단위 입력
    print()
    print("Hint : {}".format(q[1].strip()))
    guess = input("Guess a character : ")
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1
        #오류 메시지
        print("Oops! Wrong~~")
        # 남은 기호 출력
        print("Now You have", turns, "times to try..")

        # winsound.PlaySound()
        # winsound.PlaySound('../00_resource/good.wav', winsound.SND_FILENAME) # 재생할 소리 파일 경로로 지정
        if turns == 0:
            print("You Dies.")

# 앞으로 하면 좋을것들 ?
# 파이썬 고급, 성능 향상을 위한 멀티 프로그래밍, 분산처리, 쓰레드, 웹소켓 통신, Clustering multi-async IO, 병렬처리 ...
# 장고, 플라스크, DataScience 분야에서, 데이터 전처리, 수집정제...