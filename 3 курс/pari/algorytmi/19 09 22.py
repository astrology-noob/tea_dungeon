def func(x, a):
    return x**a + x**(1/2)

def solve_equation(a: int, c:int):
    min_x = 0
    max_x = c
    x = max_x / 2

    while(func(x, a) != c):
        if (func(x, a) < c):
            min_x = x
        else:
            max_x = x

        x = (min_x + max_x) / 2
    
    return round(x, 6)

print(solve_equation(3, 61))