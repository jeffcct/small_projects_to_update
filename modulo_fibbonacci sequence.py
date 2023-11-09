def fib_by_mod(mod_group):
    seen = {(0, 1): 0}
    sequence = '0, 1, 1'
    next_val = 1
    current = 1
    prev = 1
    iteration = 0
    while (current, next_val) not in seen:
        seen[(prev, current)] = iteration
        iteration += 1
        
        prev = current
        current = next_val
        next_val = (prev + current) % mod_group
        
        sequence = sequence + ", {}".format(next_val)
    seen[(prev, current)] = iteration
    if (current, next_val) != (0, 1):
        print((current, next_val), mod_group)

    return sequence
        

def main():
    for modulo_group in range(2, 100000):
        fib_by_mod(modulo_group)
    

main()
    
