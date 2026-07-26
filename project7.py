def swap_three_numbers(a, b, c):
    print(f"Original values: a = {a}, b = {b}, c = {c}")
    
    
    a, b, c = b, c, a
    
    print(f"Swapped values:  a = {a}, b = {b}, c = {c}")
    return a, b, c

value1 = 10
value2 = 25
value3 = 50

swap_three_numbers(value1, value2, value3)