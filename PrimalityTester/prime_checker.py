import time

import TrialDivision as td
import OptimizedTrialDivision as otd
import FermatLittleTheorem as flt

numbers = [2, 3, 5, 17, 29, 599, 601, 7919, 65537, 4257452468389, 425745318797,
63329620179893506339290999008541821117,
110996404203882007718023019011526260523
]

for number in numbers:
    print(f"---{number}---")
    print(td.is_prime(number))
    print(otd.is_prime(number))
    print(flt.is_prime(number, 1))