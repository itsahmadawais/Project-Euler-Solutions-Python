"""
Problem # 5:
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



Problem URL URL: https://projecteuler.net/problem=5

Code By: Awais Ahmad
Github: @itsahmadawais
Website: https://github.com/itsahmadawais
"""
def solution(step):
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

print(solution(20))