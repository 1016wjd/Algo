# 문제풀때마다 두 줄은 항상 필요
import sys
sys.stdin = open('input.txt')

char = input()

if  char.isupper():
    print(f'{char} 는 대문자 입니다.')
else:
    print(f'{char} 는 소문자 입니다.')