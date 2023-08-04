import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    

    result = []

    while len(numbers):
        
        max_num = 0
        for m in range(len(numbers)):
            if max_num < numbers[m]:
                max_num = numbers[m]

        result.append(max_num)  
        numbers.remove(max_num)


        min_num = 10000000000000
        for n in range(len(numbers)):
            if min_num > numbers[n]:
                min_num = numbers[n]

        result.append(min_num)  
        numbers.remove(min_num)

        if len(result) == 10:
            break


    print(result)
        






    
    
