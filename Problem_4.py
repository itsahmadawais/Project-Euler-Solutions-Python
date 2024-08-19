"""
Problem # 4:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.


Problem URL URL: https://projecteuler.net/problem=4

Code By: Awais Ahmad
Github: @itsahmadawais
Website: https://github.com/itsahmadawais
"""
def solution():
    max = 0
    for x in range(100,999):
        for y in range(100,999):
            val = x * y
            if(str(val)==str(val)[::-1]):
                if(val>max):
                    max = val
    return max

print(solution())