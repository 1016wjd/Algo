#sol1
def solution(my_string, letter):
    answer = ''

    for string in my_string:
        if string != letter:
            answer +=string


    return answer


#sol2
def solution(my_string, letter):
    answer = ''
    answer = my_string.replace(letter,"")
    return answer
