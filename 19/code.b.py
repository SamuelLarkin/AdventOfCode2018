#!/usr/bin/env python3
'''
This problem is about finding the sum of factors of a number.
'''

from __future__ import print_function

from computer import Computer
from factors import factor_generator
from collections import Counter

# [Finding sum of factors of a number using prime factorization](https://math.stackexchange.com/questions/163245/finding-sum-of-factors-of-a-number-using-prime-factorization)
# 1225=5^2⋅7^2, therefore the sum of factors is (1+5+25)(1+7+49)=1767
# [Finding the Sum of the Factors of a Number](http://mathforum.org/library/drmath/view/71550.html)




if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        computer = Computer()
        computer.load_instructions(f)
        assert len(computer.instructions) == 36

    computer.registers[0] = 1
    #computer.compute()
    #print('Answer:', computer.registers[0])

    counts = Counter(factor_generator(10551315))
    print(counts)
    answer = 1
    for factor, occurrence in counts.items():
        a = 1
        for i in range(occurrence):
            a += int(factor ** (i+1))
        answer *= a
    print('Answer:', answer)
    # 17427456

    # 10551315 = 5 X 3 X 31 X 22691
    # (3^0 + 3^1) X (5^0 + 5^1) X (31^0 + 31^1) X (22691^0 + 22691^1)
    # 17427456 = 4 X 6 X 32 X 22691


'''
[0, 10551315, 8, 1, 0, 1258091]
[0, 10551315, 9, 1, 0, 1258091]
[0, 10551315, 10, 1, 0, 1258091]
[0, 10551315, 2, 1, 0, 1258091]
[0, 10551315, 3, 1, 1258091, 1258091]
[0, 10551315, 4, 1, 0, 1258091]
[0, 10551315, 5, 1, 0, 1258091]
[0, 10551315, 7, 1, 0, 1258091]
[0, 10551315, 8, 1, 0, 1258092]
[0, 10551315, 9, 1, 0, 1258092]
[0, 10551315, 10, 1, 0, 1258092]
[0, 10551315, 2, 1, 0, 1258092]
[0, 10551315, 3, 1, 1258092, 1258092]
[0, 10551315, 4, 1, 0, 1258092]
[0, 10551315, 5, 1, 0, 1258092]
[0, 10551315, 7, 1, 0, 1258092]
[0, 10551315, 8, 1, 0, 1258093]
[0, 10551315, 9, 1, 0, 1258093]
[0, 10551315, 10, 1, 0, 1258093]
[0, 10551315, 2, 1, 0, 1258093]
[0, 10551315, 3, 1, 1258093, 1258093]
[0, 10551315, 4, 1, 0, 1258093]
[0, 10551315, 5, 1, 0, 1258093]
[0, 10551315, 7, 1, 0, 1258093]
'''
