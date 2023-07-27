import sys
sys.stdin = open('input.txt')

char = input()

print(char)
print(ord(char))
# print(f'(ASCII: {A})')
# print(char and f'(ASCII: {A})')

if char.isupper():
    #대문자인경우
    result = char.lower() 
    print( f'{result}(ASCII: {A})')
elif char.islower():
    #소문자인경우
        result = char.upper()
        print( f{result}'(ASCII: {A})')
else:
    #그 외의 경우
    print(char)