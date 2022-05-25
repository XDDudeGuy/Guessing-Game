from random import randint as r
from random import seed as s

def rand_num(minimum: int, maximum: int) -> int:
    for _ in range(0,100):
        s(r(minimum, maximum))
    return r(minimum, maximum)