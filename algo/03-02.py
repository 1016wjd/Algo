## 함수
def  add_data(friend):
    # 1단계 빈칸추가
    katok.append(None)
    KLen = len(katok)

    # 2단계 마지막 칸에 친구 추가
    katok[KLen-1] = friend

def insert_data(position, friend):
    # 1단계 빈칸추가
    katok.append(None)
    KLen = len(katok)

    # 2단계 한칸씩 오른쪽 이동 
    for i in range(KLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

def delete_data(position):
    # 제거
    katok[position] = None
    KLen = len(katok)
    # 한칸씩 왼쪽 이동 
    for i in range(position+1,KLen,1):
        katok[i-1] = katok[i]
        katok[i] = None
    # 마지막 none 없애주기
    del (katok[KLen-1])
    

## 변수
katok = []

## 메인 
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

# print(katok)

add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)