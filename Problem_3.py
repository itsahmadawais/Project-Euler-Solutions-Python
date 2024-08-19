"""
Problem # 3:
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?


Problem URL URL: https://projecteuler.net/problem=3

Code By: Awais Ahmad
Github: @itsahmadawais
Website: https://github.com/itsahmadawais
"""
def solution(num):
    div = int(num/2)
    list_item = []
    for x in range(2,div):
        if(num<=1):
            break
        if(num%x==0):
            num = num/x
            list_item.append(x)
    return max(list_item)

print(solution(600851475143))