counter = 0

counter2 = 0
memo = [None] * 100


# TOP DOWN
# first thing we try to solve is the highest number --> fib(n), and then eventually fib(0)
def fib(n):
    global counter
    counter += 1
    
    if memo[n] is not None:
        return memo[n]
    
    
    if n == 0 or n == 1:
        return n 
    
    memo[n] = fib(n - 1) +  fib(n - 2)
    return memo[n]
    
    

def fib_bottom_up(n):
    fib_list = [0, 1]
    
    global counter2
    
    for index in range(2, n + 1):
        counter2 += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    
    return fib_list[n]
    

print('Fibonacci TOP DOWN:')
print(fib(99))
print("Function was called", counter, "times.")

print('Fibonacci BOTTOM UP:')
print(fib_bottom_up(99))
print("Function was called", counter2, "times.")