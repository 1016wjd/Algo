import sys
sys.stdin = open('input.txt',encoding='utf-8')

man1 = input()
man2 = input()


#모든 경우의 수를 적는 방법
# if Man1 == '가위' and Man2 == '가위':
#     print('Result : Draw')
# elif Man1 == '가위' and Man2 == '바위':
#     print('Result : Man2 Win!')
# elif Man1 == '가위' and Man2 == '보':
#     print('Result : Man1 Win!')


#가위 바위 보 인덱스 생성
#0  1   2

#가위, (바위) win2  -1  
#(가위), 보   win1  -2
#바위, (보)   win2  -1
#(바위), 가위 win1   1
#보, (가위)   win2   2
#(보), 가위   win1   2



rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('Result : Man2 Win!')
    else:
        print('Result : Mam1 Win!')