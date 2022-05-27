# 파일 읽기 및 쓰기

# 읽기 모드 : r
# 쓰기 모드 : w
# 추가 모드 : a (append)
# 텍스트 모드 : t
# 바이너리 모드 : b
# 상대 경로 ( '../ , ./ '), 절대경로 (' C:\Django\example..' )

# 파일 읽기(Read)
# f = open('C:\Users\jack9\PycharmProjects\Inflearn_Original_python\resource\it_news.txt')    # 파일을 연결
f = open('../resource/it_news.txt', 'r', encoding='UTF-8')  # t 는 default 라서 skip 해도 됨.

# 속성 확인
print(dir(f))
# ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']

# 인코딩 확인
print(f.encoding)
print(f.name)

# 모드 확인
print(f.mode)

contents = f.read()
# print(contents)
# 쓴것은 반드시 닫아야 합니다.
f.close()
print()
# 보통은 f 로 open 해서 사용하기보다 with 문을 쓴다.
with open('../resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))  #<str_iterator object at 0x0000028A21C52F40>
    # close를 호출하지 않아도 내부적으로 connection 이 닫힙니다.
print()

# read() : 전체 읽기, read(10) : 10Byte int형에 맞는 byte 수만큼만 읽어옴
with open('../resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)      # 20 Byte 만 받아옵니다.
    print(c)
    c = f.read(20)      # 20 Byte 이후인 부분에 커서가 기억하고 있고, 커서부터 20byte 만큼 읽어옵니다.
    print(c)
    f.seek(0,0)         # 처음으로 돌아간다. ( from, to )
    c = f.read(20)
    print(c)
print()

# readline \n 을 인식해서 한 줄씩 읽어옵니다.
with open('../resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()     # 한줄 출력
    print(line)
    line = f.readline()     # 다음줄 출력
    print(line)
print()

# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('../resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cont = f.readlines()
    # print(cont)
    # print(cont[1])
    for i in cont:
        print(i, end=' ')



